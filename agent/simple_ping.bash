#!/usr/bin/env bash

source "$(dirname "$0")"/../config.bash
my_public_ip="$(curl ipecho.net/plain --silent)"

if [ -n "$CACERT" ] ; then
    CACERT="--cacert $CACERT"
else
    CACERT=
fi

if [ -n "$SIMPLE_PING_KEY" ] ; then
    SIMPLE_PING_KEY="&key=$SIMPLE_PING_KEY"
else
    SIMPLE_PING_KEY=
fi

url="https://$MANAGER_IP:$MANAGER_PORT/simple_ping?public_ip=$my_public_ip$SIMPLE_PING_KEY"

response=$(
curl \
    "$url" \
    --silent \
    $CACERT
)

if [ "$response" = "404" ] ; then
    echo "failed to connect to manager"
fi
