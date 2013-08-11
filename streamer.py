import os

import twitter

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
    	message = "I got this too! ({0})".format(msg['direct_message'])
        t.direct_messages.new(user=ENV['TWITTER_HANDLE'],
        	text=message)