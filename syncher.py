#!/usr/local/bin/python

#######
#  Syncher.py
#
#  Reads info from Withings account and syncs to fitbit account

import json as js
import os.path

global CONFIG_FNAME
global CONFIG_FD
CONFIG_FNAME = '~/config.json'


def initialize_withings_config_file():
    CONFIG_FD = open(CONFIG_FNAME, 'w+')

    config = dict()
    config['withings'] = dict()
    config['fitbit'] = dict()

    config['withings']['user_name'] = 'User'
    config['withings']['user_id'] = '12345'

    config['fitbit']['user_name'] = 'User'
    config['fitbit']['user_id'] = '12345'

    js.JSONEncoder()




def main():
    #create config file if it doesn't exist
    if not os.path.isfile(CONFIG_FNAME):
        CONFIG_FD = initialize_withings_config_file()
    else:
        CONFIG_FD = open(CONFIG_FNAME, 'r+')









