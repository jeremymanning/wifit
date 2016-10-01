#!/usr/local/bin/python

#######
#  Syncher.py
#
#  Reads info from Withings account and syncs to fitbit account

import json as js
import os.path
from withings import WithingsAuth, WithingsApi
import fitbit as fb
import datetime as dt

global CONFIG_FNAME
global CONFIG_FD
CONFIG_FNAME = '~/config.json'

class FitInfo:
    def __init__(self, configfile=CONFIG_FNAME):
        self.config = configfile
        self.withings = WithingsFitInfo(configfile=configfile)
        self.fitbit = FitbitFitInfo(configfile=configfile)

class WithingsFitInfo:
    def __init__(self, configfile):
        config = get_config(configfile) #TODO: write this function
        auth = WithingsAuth(config['withings']['key'], config['withings']['secret'])
        authorize_url = auth.get_authorize_url()
        print "Go to %s allow the app and copy your oauth_verifier" % authorize_url

        oauth_verifier = raw_input('Please enter your oauth_verifier: ')
        creds = auth.get_credentials(oauth_verifier)

        client = WithingsApi(creds)
        data = client.get_measures()

        #activity
        self.date = data[0].date
        self.steps = data[0].steps
        self.distance = data[0].distance
        self.calories = data[0].calories
        self.totalcalories = data[0].totalcalories
        self.elevation = data[0].elevation
        self.soft = data[0].soft
        self.moderate = data[0].moderate
        self.intense = data[0].intense
        self.status = data[0].status

        #sleep
        self.wakeupduration = data[0].wakeupduration
        self.lightsleepduration = data[0].lightsleepduration
        self.deepsleepduration = data[0].deepsleepduration
        self.remsleepduration = data[0].remsleepduration
        self.wakeupcount = data[0].wakeupcount
        self.durationtosleep = data[0].durationtosleep
        self.durationtowake = data[0].durationtowake

class FitbitFitInfo:
    def __init__(self, configfile=CONFIG_FNAME):
        config = get_config(configfile)  # TODO: write this function
        unauth_client = fitbit.Fitbit(config['fitbit']['key'], config['fitbit']['secret'])
        authd_client = fitbit.Fitbit(config['fitbit']['key'], config['fitbit']['secret'],
                                     access_token=config['fitbit']['access_token'],
                                     refresh_token=config['fitbit']['refresh_token'])

        #fill in info: http://python-fitbit.readthedocs.io/en/latest/




def initialize_withings_config_file():
    CONFIG_FD = open(CONFIG_FNAME, 'w+')

    config = dict()
    config['withings'] = dict()
    config['fitbit'] = dict()

    config['withings']['key'] = 'User'
    config['withings']['secret'] = '12345'

    config['fitbit']['key'] = 'User'
    config['fitbit']['secret'] = '12345'

    js.JSONEncoder()




def main():
    #create config file if it doesn't exist
    if not os.path.isfile(CONFIG_FNAME):
        CONFIG_FD = initialize_withings_config_file()
    else:
        CONFIG_FD = open(CONFIG_FNAME, 'r+')









