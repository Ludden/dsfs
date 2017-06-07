import json
from collections import Counter

from twython import TwythonStreamer

key = json.loads(open("credentials.json").read())["key"]
secret = json.loads(open("credentials.json").read())["secret"]
token = json.loads(open("credentials.json").read())["token"]
token_secret = json.loads(open("credentials.json").read())["token-secret"]

tweets = []


class TwitterStreamer(TwythonStreamer):
    def on_success(self, data):
        if data['lang'] == 'en':
            tweets.append(data)
            print "received tweet #", len(tweets), data

        if len(tweets) > 100:
            self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()


stream = TwitterStreamer(key, secret, token, token_secret)
stream.statuses.filter(track='sparksummit')
stream.statuses.sample()

top_hashtags = Counter(hashtag['text'].lower()
                       for tweet in tweets
                       for hashtag in tweet["entities"]["hashtags"])

print top_hashtags.most_common(5)
