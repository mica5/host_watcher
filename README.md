# host_watcher
basic tools for watching hosts and devices over a network

# About

This follows the same vocabulary as OSSEC HIDS, "manager" and "agent".

# Setup

    cp config.bash.example config.bash
    # populate config.bash

# Manager setup

    # from the server:
    source manager/environment.bash
    pip3 install --requirement manager/python_requirements.txt

    # uses python alembic to create or update db to the latest version
    python3 manager/database/setup_or_update.py

    # gunicorn server to listen from agents
    python3 manager/start_listener.py

# Agent setup



# Agent setup, simple version

    # first make sure that it's working
    python3 agent/simple_ping.py

    # then put this on a cron job:
    * * * * * path/to/python3 agent/simple_ping.py
