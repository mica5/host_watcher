#!/usr/bin/env python
"""Create a repository for a new agent

Version 0.1
datestr
"""
import argparse
import os
import subprocess

def run_main():
    args = parse_cl_args()

    subprocess.call("""
    {echo} cd "{crontab_dir}"
    {echo} mkdir "{name}"
    {echo} cd "{name}"
    {echo}  git init
    """.format(
        name=args.name,
        crontab_dir=os.path.dirname(os.path.abspath(__file__)),
        echo='echo' if args.dry_run else '',
    ), shell=True)

    success = True
    return success

def parse_cl_args():
    argParser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    argParser.add_argument('name')
    argParser.add_argument(
        '--dry-run', default=False, action='store_true',
    )

    args = argParser.parse_args()
    return args


if __name__ == '__main__':
    success = run_main()
    exit_code = 0 if success else 1
    exit(exit_code)
