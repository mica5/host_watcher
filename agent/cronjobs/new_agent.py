#!/usr/bin/env python
"""Create a repository for a new agent

Version 0.1
2018-07-26
"""
import argparse
import os
import subprocess
from config import user, manager, cronjob_repo_path_on_manager

def run_main():
    args = parse_cl_args()

    subprocess.call("""
    CRONJOB_REPO="{cronjob_repo}"
    ssh {user}{manager} <<EOF
        mkdir --parents $CRONJOB_REPO
        cd $CRONJOB_REPO
        git init
    \nEOF\n
    """.format(
        user='{}@'.format(user) if user else '',
        manager=manager,
        cronjob_repo=cronjob_repo_path_on_manager,
    ), shell=True)

    success = True
    return success

def parse_cl_args():
    argParser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    args = argParser.parse_args()
    return args


if __name__ == '__main__':
    success = run_main()
    exit_code = 0 if success else 1
    exit(exit_code)
