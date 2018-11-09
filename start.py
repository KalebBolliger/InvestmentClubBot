import tweepy
import json

# get twitter keys
with open("auth_twitter.json") as file_twitter:
	twitter_auth = json.load(file_twitter)

tw_consumer_key = twitter_auth["consumer"]
tw_consumer_secret = twitter_auth["consumer_secret"]
tw_token_key = twitter_auth["token"]
tw_token_secret = twitter_auth["token_secret"]

# tweepy authentication
auth = tweepy.OAuthHandler(tw_consumer_key, tw_consumer_secret)
auth.set_access_token(tw_token_key, tw_token_secret)
api = tweepy.API(auth)

# send tweet
status = "Hello world!"
api.update_status(status=status)
