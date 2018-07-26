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

    manager_cronjobs_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(manager_cronjobs_dir)

    echo = 'echo' if args.dry_run else ''
    if args.user:
        chown = '{echo} sudo chown -R {user}:{user} agents/{name}'.format(
            echo=echo,
            user=args.user,
            name=args.name,
        )
    else:
        chown = ''

    subprocess.call("""
    # "agents" directory already exists because it's
    # part of the repository
    {echo} mkdir agents/"{name}"
    {echo} cd agents/"{name}"
    {echo} git init
    {echo} eval 'cd - > /dev/null'
    {chown}
    """.format(
        chown=chown,
        name=args.name,
        echo=echo,
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
       'user', nargs='?',
        help='user on manager who will (ch)own the cronjob repository.'
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
