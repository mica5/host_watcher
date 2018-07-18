#!/usr/bin/env bash

source "$(dirname "$0")"/../config.bash
my_public_ip="$(curl ipecho.net/plain --silent)"

curl --silent "https://$MANAGER_IP:$MANAGER_PORT/simple_ping?public_ip=$my_public_ip"
