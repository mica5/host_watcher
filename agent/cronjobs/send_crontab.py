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

from config import user, manager, manager_port, cronjob_repo_path_on_manager


def run_main():
    args = parse_cl_args()

    port = '-p ' + manager_port if manager_port else ''
    user = user+'@' if user else ''

    command = """
        \ncrontab -l | ssh {user}{manager} {port} 'cat > {cronjob_repo_path_on_manager}/crontab.txt'
        \nssh {user}{manager} {port} <<EOF
            cd {cronjob_repo_path_on_manager}
            git add crontab.txt
            git commit -m "autocommit from host_watcher/agent/cronjobs/send_crontab.py"
        \nEOF\n
    """.format(
        user=user,
        manager=manager,
        port=port,
        cronjob_repo_path_on_manager=cronjob_repo_path_on_manager,
    )
    if args.dry_run:
        print(command.lstrip())
    else:
        subprocess.call(command, shell=True)

    success = True
    return success

def parse_cl_args():
    argParser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    argParser.add_argument(
        '--dry-run', default=False, action='store_true',
    )

    args = argParser.parse_args()
    return args


if __name__ == '__main__':
    success = run_main()
    exit_code = 0 if success else 1
    exit(exit_code)
