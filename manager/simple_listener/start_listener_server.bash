#!/usr/bin/env bash


listener_server="$(ls "$(dirname "$0")"/listener_server.py)"
listener_server="${listener_server%.py}"
listener_server="${listener_server//\//.}"
listener_server="$(echo $listener_server | sed 's/^\.*//')"

source "$(dirname "$0")"/../../config.bash

pid_file="$(dirname "$0")"/https.pid

if [ -n "$DEBUG" ] && $DEBUG ; then
    DAEMON=
    LOG_FILE=
else
    log_file="$(dirname "$0")"/log.txt
    if [ ! -e "$log_file" ] ; then
        touch "$log_file"
    fi
    LOG_FILE="--log-file $log_file"
    if $DAEMON ; then
        DAEMON=-D
    else
        DAEMON=
    fi
fi

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
    --pid "$pid_file" \
    $LOG_FILE \
    $DAEMON \
    $SSL_CERTIFICATE \
    $SSL_KEYFILE \
    $EXTRA_GUNICORN_ARGS \
    $listener_server:api
