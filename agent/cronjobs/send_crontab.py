#!/usr/bin/env python
"""Send crontab to a manager

Version 0.1
2018-07-26
"""
import sys
import os

import argparse
import subprocess

this_dir = os.path.dirname(os.path.abspath(__file__))
if this_dir not in sys.path:
    sys.path.insert(0, this_dir)

from config import user, manager, host_watcher_repo_on_manager, this_agent_name

def run_main():
    args = parse_cl_args()

    command = """
        crontab -l | ssh {user}{manager} '{host_watcher_repo_on_manager}/manager/cronjobs/update_cronjob.py {name}'
        """.format(
            user='{}@'.format(user) if user else '',
            manager=manager,
            host_watcher_repo_on_manager=host_watcher_repo_on_manager,
            name=this_agent_name,
    )
    if args.dry_run:
        print(command)
    else:
        subprocess.call(command, shell=True)

    success = True
    return success

def parse_cl_args():
    argParser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    argParser.add_argument('--dry-run', default=False, action='store_true')

    args = argParser.parse_args()
    return args


if __name__ == '__main__':
    success = run_main()
    exit_code = 0 if success else 1
    exit(exit_code)
