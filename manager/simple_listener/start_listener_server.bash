#!/usr/bin/env bash

source "$(dirname "$0")"/../../config.bash

pid_file="$(dirname "$0")"/https.pid

if [ -n "$DEBUG" ] && $DEBUG ; then
    DAEMON=
    log_file=
else
    log_file="$(dirname "$0")"/log.txt
    if $DAEMON ; then
        DAEMON=-D
    else
        DAEMON=
    fi
fi
LOG_FILE="--log-file \"$log_file\""


if [ -n "$SSL_CERTIFICATE" ] ; then
    SSL_CERTIFICATE="--certfile $SSL_CERTIFICATE"
else
    SSL_CERTIFICATE=
fi

if [ -n "$SSL_KEYFILE" ] ; then
    SSL_KEYFILE="--keyfile $SSL_KEYFILE"
else
    SSL_KEYFILE=
fi

gunicorn \
    -b $MANAGER_LISTEN_IP:$MANAGER_PORT \
    $DAEMON \
    --pid "$pid_file" \
    "$LOG_FILE" \
    "$SSL_CERTIFICATE" \
    "$SSL_KEYFILE"
