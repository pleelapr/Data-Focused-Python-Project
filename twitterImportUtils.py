import tweepy
from tweepy import OAuthHandler
import pymongo
from bson import json_util
import json
import pandas as pd
import time
import os

ts = time.time()

PATH_RESULT = 'result'

consumer_key = 'DrGOIXEKRwMecmdGsPO8C9GuV'
consumer_secret = 'I8KTilKpecXVW9BEjkHu2OqXVZoXAPXy3PIKR0KplQ75yMoq7w'
access_token = '264665590-ZQUkBKt8LuPtpJGJ21rQGDg842rCojtmCYBbcGnP'
access_token_secret = 'sSMrpla9SRtQs76298XjR0p3nUVxobGs7FyTJXth2F77U'
# Authenticate twitter Api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#made a cursor
c = tweepy.Cursor(api.search, q='%23AAPL')
c.pages(500) # you can change it make get tweets

#Lets save the selected part of the tweets inot json
tweetJson = []
for tweet in c.items():
    if tweet.lang == 'en':
        createdAt = str(tweet.created_at)
        authorCreatedAt = str(tweet.author.created_at)
        tweetJson.append(
          {'tweetText':tweet.text,
          'tweetCreatedAt':createdAt,
          'authorName': tweet.author.name,
          'location': tweet.author.name,
          })
#dump the data into json format

tweet_df = pd.DataFrame(tweetJson)

tweet_df.to_csv(os.path.join(PATH_RESULT,str(ts)+'_'+'tweets.csv'), index=False)
# print(json.dumps(tweetJson))

print(tweet_df)