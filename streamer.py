import os

import twitter
import requests


auth = twitter.OAuth(
            consumer_key=os.environ['CONSUMER_KEY'],
            consumer_secret=os.environ['CONSUMER_SECRET'],
            token=os.environ['TOKEN_KEY'],
            token_secret=os.environ['TOKEN_SECRET']
        )

twitter_userstream = twitter.TwitterStream(auth=auth,
    domain='userstream.twitter.com')

for msg in twitter_userstream.user():
    if 'direct_message' in msg:
    	if msg['direct_message']['sender_screen_name'] != "shelvd":
	    	input_text = msg['direct_message']['text']
            message = ("I got this too! ({0})").format(input_text)
	    	t = twitter.Twitter(auth=auth)
	        t.direct_messages.new(user=os.environ['TWITTER_HANDLE'],
	        	text=message)
            requests.post("http://shelvd.herokuapp.com/", data={
                "bkinput": input_text, "source": "twitter"})
