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

#create config file if it doesn't exist
if not os.path.isfile(CONFIG_FNAME):
    CONFIG_FD = initialize_config_file()
else:
    CONFIG_FD = open(CONFIG_FNAME, 'r+')

def initialize_config_file():
    userName = 'User'
    userID = '12345'
    

