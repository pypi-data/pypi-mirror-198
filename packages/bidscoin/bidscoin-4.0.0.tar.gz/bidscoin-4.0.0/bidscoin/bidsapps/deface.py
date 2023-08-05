#!/usr/bin/env python3
"""
A wrapper around the 'pydeface' defacing tool (https://github.com/poldracklab/pydeface).

Except for BIDS inheritances and IntendedFor usage, this wrapper is BIDS-aware (a 'bidsapp')
and writes BIDS compliant output

Linux users can distribute the computations to their HPC compute cluster if the DRMAA
libraries are installed and the DRMAA_LIBRARY_PATH environment variable set

For multi-echo data see `medeface`
"""

import os
import shutil
import argparse
import json
import logging
import pandas as pd
import pydeface.utils as pdu
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm
from pathlib import Path
try:
    from bidscoin import bcoin
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).parents[1]))             # This should work if bidscoin was not pip-installed
    import bcoin


def deface(bidsdir: str, pattern: str, subjects: list, force: bool, output: str, cluster: bool, nativespec: str, kwargs: dict):
    """
    :param bidsdir:     The bids-directory with the subject data
    :param pattern:     Globlike search pattern (relative to the subject/session folder) to select the images that need to be defaced, e.g. 'anat/*_T1w*'
    :param subjects:    List of sub-# identifiers to be processed (the sub-prefix can be left out). If not specified then all sub-folders in the bidsfolder will be processed
    :param force:       If True then images will be processed, regardless if images have already been defaced (i.e. if {"Defaced": True} in the json sidecar file)
    :param output:      Determines where the defaced images are saved. It can be the name of a BIDS datatype folder, such as 'anat', or of the derivatives folder, i.e. 'derivatives'. If output is left empty then the original images are replaced by the defaced images
    :param cluster:     Flag to submit the deface-jobs to the high-performance compute (HPC) cluster using the drmaa library
    :param nativespec:  DRMAA native specifications for submitting deface jobs to the HPC cluster
    :param kwargs:      Additional arguments (in dict/json-style) that are passed to pydeface. See examples for usage
    :return:
    """

    # Input checking
    bidsdir = Path(bidsdir).resolve()
    if not bidsdir.is_dir():
        print(f"Could not find the bids folder: {bidsdir}")
        return

    # Start logging
    bcoin.setup_logging(bidsdir/'code'/'bidscoin'/'deface.log')
    LOGGER.info('')
    LOGGER.info('------------ START deface ------------')
    LOGGER.info(f">>> deface bidsfolder={bidsdir} pattern={pattern} subjects={subjects} output={output}"
                f" cluster={cluster} nativespec={nativespec} {kwargs}")

    # Get the list of subjects
    if not subjects:
        subjects = bcoin.lsdirs(bidsdir, 'sub-*')
        if not subjects:
            LOGGER.warning(f"No subjects found in: {bidsdir/'sub-*'}")
    else:
        subjects = ['sub-' + subject.replace('sub-', '') for subject in subjects]               # Make sure there is a "sub-" prefix
        subjects = [bidsdir/subject for subject in subjects if (bidsdir/subject).is_dir()]

    # Prepare the HPC job submission
    if cluster:
        from drmaa import Session as drmaasession
    else:
        from contextlib import nullcontext as drmaasession                                      # Use a dummy context manager
    with drmaasession() as pbatch:
        if cluster:
            jt                     = pbatch.createJobTemplate()
            jt.jobEnvironment      = os.environ
            jt.remoteCommand       = shutil.which('pydeface')
            jt.nativeSpecification = nativespec
            jt.joinFiles           = True

        # Loop over bids subject/session-directories
        with logging_redirect_tqdm():
            for n, subject in enumerate(tqdm(subjects, unit='subject', leave=False), 1):

                subid    = subject.name
                sessions = bcoin.lsdirs(subject, 'ses-*')
                if not sessions:
                    sessions = [subject]
                for session in sessions:

                    LOGGER.info('--------------------------------------')
                    LOGGER.info(f"Processing ({n}/{len(subjects)}): {session}")

                    # Search for images that need to be defaced
                    sesid = session.name if session.name.startswith('ses-') else ''
                    for match in sorted([match for match in session.glob(pattern) if '.nii' in match.suffixes]):

                        # Construct the output filename and relative path name (used in BIDS)
                        match_rel = match.relative_to(session).as_posix()
                        if not output:
                            outputfile     = match
                            outputfile_rel = match_rel
                        elif output == 'derivatives':
                            srcent, suffix = match.with_suffix('').stem.rsplit('_', 1)  # Name without suffix, suffix
                            ext = ''.join(match.suffixes)                               # Account for e.g. '.nii.gz'
                            outputfile     = bidsdir/'derivatives'/'deface'/subid/sesid/match.parent.name/f"{srcent}_space-orig_{suffix}{ext}"
                            outputfile_rel = outputfile.relative_to(bidsdir).as_posix()
                        else:
                            outputfile     = session/output/match.name
                            outputfile_rel = outputfile.relative_to(session).as_posix()
                        outputfile.parent.mkdir(parents=True, exist_ok=True)

                        # Check the json "Defaced" field to see if it has already been defaced
                        outputjson = outputfile.with_suffix('').with_suffix('.json')
                        if not force and outputjson.is_file():
                            with outputjson.open('r') as sidecar:
                                metadata = json.load(sidecar)
                            if metadata.get('Defaced'):
                                LOGGER.info(f"Skipping already defaced image: {match_rel} -> {outputfile_rel}")
                                continue

                        # Deface the image
                        LOGGER.info(f"Defacing: {match_rel} -> {outputfile_rel}")
                        if cluster:
                            jt.args    = [str(match), '--outfile', str(outputfile), '--force'] + [item for pair in [[f"--{key}",val] for key,val in kwargs.items()] for item in pair]
                            jt.jobName = f"pydeface_{subid}_{sesid}"
                            jobid      = pbatch.runJob(jt)
                            LOGGER.info(f"Your deface job has been submitted with ID: {jobid}")
                        else:
                            pdu.deface_image(str(match), str(outputfile), force=True, forcecleanup=True, **kwargs)

                        # Add a json sidecar-file with the "Defaced" field
                        inputjson = match.with_suffix('').with_suffix('.json')
                        if inputjson.is_file():
                            with inputjson.open('r') as sidecar:
                                metadata = json.load(sidecar)
                        else:
                            metadata = {}
                        metadata['Defaced'] = True
                        with outputjson.open('w') as sidecar:
                            json.dump(metadata, sidecar, indent=4)

                        # Update the scans.tsv file
                        scans_tsv  = session/f"{subid}{'_'+sesid if sesid else ''}_scans.tsv"
                        bidsignore = (bidsdir/'.bidsignore').read_text().splitlines() if (bidsdir/'.bidsignore').is_file() else ['extra_data/']
                        if output and output+'/' not in bidsignore + ['derivatives/'] and scans_tsv.is_file():
                            LOGGER.info(f"Adding {outputfile_rel} to {scans_tsv}")
                            scans_table                     = pd.read_csv(scans_tsv, sep='\t', index_col='filename')
                            scans_table.loc[outputfile_rel] = scans_table.loc[match_rel]
                            scans_table.sort_values(by=['acq_time','filename'], inplace=True)
                            scans_table.to_csv(scans_tsv, sep='\t', encoding='utf-8')

        if cluster:
            LOGGER.info('')
            LOGGER.info('Waiting for the deface jobs to finish...')
            pbatch.synchronize(jobIds=[pbatch.JOB_IDS_SESSION_ALL], timeout=pbatch.TIMEOUT_WAIT_FOREVER, dispose=True)
            pbatch.deleteJobTemplate(jt)

    LOGGER.info('-------------- FINISHED! -------------')
    LOGGER.info('')


def main():
    """Console script usage"""

    class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter): pass

    parser = argparse.ArgumentParser(formatter_class=CustomFormatter,
                                     description=__doc__,
                                     epilog='examples:\n'
                                            '  deface myproject/bids anat/*_T1w*\n'
                                            '  deface myproject/bids anat/*_T1w* -p 001 003 -o derivatives\n'
                                            '  deface myproject/bids anat/*_T1w* -c -n "-l walltime=00:60:00,mem=4gb"\n'
                                            '  deface myproject/bids anat/*_T1w* -a \'{"cost": "corratio", "verbose": ""}\'\n ')
    parser.add_argument('bidsfolder',               help='The bids-directory with the subject data')
    parser.add_argument('pattern',                  help="Globlike search pattern (relative to the subject/session folder) to select the images that need to be defaced, e.g. 'anat/*_T1w*'")
    parser.add_argument('-p','--participant_label', help='Space separated list of sub-# identifiers to be processed (the sub-prefix can be left out). If not specified then all sub-folders in the bidsfolder will be processed', nargs='+')
    parser.add_argument('-o','--output',            help=f"A string that determines where the defaced images are saved. It can be the name of a BIDS datatype folder, such as 'anat', or of the derivatives folder, i.e. 'derivatives'. If output is left empty then the original images are replaced by the defaced images")
    parser.add_argument('-c','--cluster',           help='Use the DRMAA library to submit the deface jobs to a high-performance compute (HPC) cluster', action='store_true')
    parser.add_argument('-n','--nativespec',        help='DRMAA native specifications for submitting deface jobs to the HPC cluster', default='-l walltime=00:30:00,mem=2gb')
    parser.add_argument('-a','--args',              help='Additional arguments (in dict/json-style) that are passed to pydeface. See examples for usage', type=json.loads, default={})
    parser.add_argument('-f','--force',             help='Deface all images, regardless if they have already been defaced (i.e. if {"Defaced": True} in the json sidecar file)', action='store_true')
    args = parser.parse_args()

    deface(bidsdir    = args.bidsfolder,
           pattern    = args.pattern,
           subjects   = args.participant_label,
           force      = args.force,
           output     = args.output,
           cluster    = args.cluster,
           nativespec = args.nativespec,
           kwargs     = args.args)


if __name__ == '__main__':
    LOGGER = logging.getLogger(f"bidscoin.{Path(__file__).stem}")
    main()

else:
    LOGGER = logging.getLogger(__name__)
