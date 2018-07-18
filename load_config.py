#!/usr/bin/env python
import subprocess
import os

this_dir = os.path.dirname(os.path.abspath(__file__))

config_file = os.path.join(
    this_dir,
    'config.bash'
)

# thanks https://stackoverflow.com/a/3505826/2821804
command = 'bash -c "{{ source {config_file} && env ; }}"'.format(
    config_file=config_file,
)
env = subprocess.check_output(
    command,
    shell=True
).decode().strip()

for line in env.split('\n'):
    line = line.strip()
    name, value = line.split('=', 1)
    os.environ[name] = value
