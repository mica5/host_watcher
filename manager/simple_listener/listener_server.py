#!/usr/bin/env python
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

    def on_get(self, req, resp):
        """Handles GET requests
        """
        public_ip = req.params.get('public_ip', 'not specified')

        logstr = '{};public_ip:{}'.format(
            datetime.datetime.now(),
            public_ip,
        )

        with open(log_file, 'a') as fa:
            print(logstr, file=fa)

api.add_route('/simple_ping', ListenResource())
