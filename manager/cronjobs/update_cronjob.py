#!/usr/bin/env python
"""

Version 0.1
2018-07-26
"""
import argparse
import os
import subprocess

def run_main():
    args = parse_cl_args()

    this_dir = os.path.dirname(os.path.abspath(__file__))
    subprocess.call("""
        cd "{this_dir}"/agents/"{name}"
        cat > crontab.txt
        git add crontab.txt
        git commit -m "autocommit by {__file__}"
    """.format(
        this_dir=this_dir,
        name=args.name,
        __file__=__file__,
    ), shell=True)

    success = True
    return success

def parse_cl_args():
    argParser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    argParser.add_argument('name')

    args = argParser.parse_args()
    return args


if __name__ == '__main__':
    success = run_main()
    exit_code = 0 if success else 1
    exit(exit_code)
