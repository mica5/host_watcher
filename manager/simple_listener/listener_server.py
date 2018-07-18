#!/usr/bin/env python
import subprocess
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from load_config import os

import datetime

import falcon


this_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(this_dir, 'log.txt')

api = falcon.API()

class ListenResource:

    do_key_auth = os.environ.get('KEY_AUTH', 'false') == 'true'
    keys = list()
    key_dict = dict()
    if do_key_auth:
        keys = subprocess.check_output(
            "ls keys.bash >/dev/null && grep -vP '^\s*#|^\s*$' keys.bash; exit 0",
            shell=True,
        ).decode().strip()
        keys = list(map(lambda x: x.strip(), keys.split('\n')))
        key_dict = dict()
        for i in range(len(keys)):
            keystr = keys[i]
            device_name, key = keystr.split('=', 1)
            key_dict[key] = device_name
        del device_name, key

    failed_auth_string = 'NONE, FAILED AUTH!'

    def on_get(self, req, resp):
        """Handles GET requests
        """
        values = ['SIMPLE_PING']

        failed_key_auth = False
        if self.do_key_auth:
            key = req.params.get('key', 'none')
            device_name = self.key_dict.get(key, self.failed_auth_string)
            if device_name == self.failed_auth_string:
                failed_key_auth = True
            values.append('device_name_from_key:{}'.format(device_name))


        public_ip_reported = req.params.get('public_ip', 'not specified')

        values.append('{}:{}'.format('time', datetime.datetime.now()))
        keys = [
            'HTTP_USER_AGENT',
            'REMOTE_ADDR',
            'REMOTE_PORT',
        ]
        for key in keys:
            values.append('{}:{}'.format(key, req.env.get(key, 'unknown')))
        values.append('{}:{}'.format('public_ip_reported', public_ip_reported))

        logstr = ';'.join(values)

        print(logstr)
        if failed_key_auth:
            resp.body = '404'
            raise falcon.errors.HTTPNotFound()

api.add_route('/simple_ping', ListenResource())
