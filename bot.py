import tweepy
from secrets import *

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 

auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

username = ''
user = api.get_user(username)

'''''''''''
for friend in user.friends():
    print(friend.screen_name)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
'''''''''''

image = 'tweet-me.png'
tweet_text = ' has given me, the bot, the permision to tweet! Bot is freee!'
api.update_with_media(image, status = 'Master ' + '@{0}'.format(username) + tweet_text)

api.update_status("I am a bot.")