import os
import logging

from twython import TwythonStreamer
import requests

class MyStreamer(TwythonStreamer):
    def on_success(self, msg):
        if 'direct_message' in msg.keys():
            if msg['direct_message']['sender_screen_name'] != "shelvd":
                logging.info(msg['direct_message']['text'])
                requests.post("http://shelvd.herokuapp.com/receive-input",
                    data={"bkinput": msg['direct_message']['text'],
                    "source": "twitter"})

    def on_error(self, status_code, data):
        logging.error(status_code)
        logging.error(data)

twitter = MyStreamer(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'],
            os.environ['TOKEN_KEY'], os.environ['TOKEN_SECRET'])

twitter.user()