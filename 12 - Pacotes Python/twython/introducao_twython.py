#INTRODUÇÃO TWYTHON

import twython
from twython import TwythonStreamer
import json

PP_KEY = credenciais['app_key']
APP_SECRET = credenciais['app_secret']

ACCESS_TOKEN = credenciais['access_token']
ACCESS_TOKEN_SECRET = credenciais['access_token_secret']

twitter = twython.Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'])

    def on_error(self, status_code, data):
        print(status_code)

stream = MyStreamer(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
stream.statuses.filter(track='twitter')