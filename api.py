#!/usr/bin/env python

import requests
import json
from pocket import Pocket, PocketException
from flaskapp import app, rest_api


class PocketAPI:

    """ Wrapper around https://pypi.python.org/pypi/pocket-api/ """

    def __init__(self, consumer_key=None, access_token=None):
        self.consumer_key = consumer_key
        self.access_token = access_token

    def get_request_token(self):
        """ Get request token: https://getpocket.com/developer/docs/authentication """
        headers = {
            'content-type': 'application/json; charset=UTF-8',
            'x-accept': 'application/json'
        }
        data = {
            'consumer_key': self.consumer_key,
            'redirect_uri': 'https://getpocket.com/v3/oauth/authorize'
        }
        pocket_api = requests.post(
            'https://getpocket.com/v3/oauth/request',
            data=json.dumps(data),
            headers=headers
        )
        r = json.loads(pocket_api.text)
        return r['code']

    def get_access_token(self, request_token):
        """ Get access token: https://getpocket.com/developer/docs/authentication """
        headers = {
            'content-type': 'application/json; charset=UTF-8',
            'x-accept': 'application/json'
        }
        data = {
            'consumer_key': self.consumer_key,
            'code': request_token
        }
        pocket_api = requests.post(
            'https://getpocket.com/v3/oauth/authorize',
            data=json.dumps(data),
            headers=headers
        )
        r = json.loads(pocket_api.text)
        return r['access_token']

    def connect(self):
        """ Connect to the getpocket API and initiate python api """

        # If access token is already provided skip this one
        if not self.access_token:
            # Get request token
            self.request_token = self.get_request_token()
            print("[*] Request token: %s" % self.request_token)
            print("Now you need to authorize this app to access your getpocket list.")
            print("Open this URL in your browser: https://getpocket.com/auth/authorize?request_token=%s&redirect_uri=https://getpocket.com" % self.request_token)
            input("Press Enter to continue...")

            # Get access token
            self.access_token = self.get_access_token(self.request_token)
            print("[*] Access token: %s" % self.access_token)

        # Create pocket-api
        self.p = Pocket(
            consumer_key=self.consumer_key,
            access_token=self.access_token
        )

    def get(self, **kwargs):
        """ Fetch list of articles """
        # Fetch a list of articles
        try:
            return self.p.retrieve(**kwargs)
        except PocketException as e:
            print(e.message)
            return None

    def test(self):
        return "bla"

if __name__ == '__main__':

    # Init pocket API
    p = PocketAPI(
        consumer_key=app.config['POCKET_CONSUMER_KEY'],
        access_token=app.config['POCKET_ACCESS_TOKEN'])
    p.connect()

    # Init and run flask API
    rest_api.set_pocket(p)
    rest_api.run()
