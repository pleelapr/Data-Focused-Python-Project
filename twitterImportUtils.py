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
# c = tweepy.Cursor(api.search, q='%23AAPL', tweet_mode='extended')
# c.pages(10000) # you can change it make get tweets

#Lets save the selected part of the tweets inot json
tweetList = []

# Mention the maximum number of tweets that you want to be extracted.
maximum_number_of_tweets_to_be_extracted = 5000

# Mention the hashtag that you want to look out for
hashtag = 'AAPL'

for tweet in tweepy.Cursor(api.search, q='%24'+hashtag, rpp=100, tweet_mode='extended').items(maximum_number_of_tweets_to_be_extracted):
	if tweet.lang == 'en':
		createdAt = str(tweet.created_at)
		authorCreatedAt = str(tweet.author.created_at)
		tweetList.append(
		{'tweetText':tweet.full_text,
		'Date':createdAt,
		'authorName': tweet.author.name,
		})
	# with open('tweets_with_hashtag_' + hashtag + '.txt', 'a') as the_file:
	# 	the_file.write(str(tweet.text.encode('utf-8')) + '\n')
tweet_df = pd.DataFrame(tweetList)
tweet_df.to_csv(os.path.join(PATH_RESULT,str(ts)+'_'+'tweets.csv'), index=False)

print ('Extracted ' + str(maximum_number_of_tweets_to_be_extracted) + ' tweets with hashtag #' + hashtag)


# for tweet in c.items():
# 	if tweet.lang == 'en':
# 		createdAt = str(tweet.created_at)
# 		authorCreatedAt = str(tweet.author.created_at)
# 		tweetJson.append(
# 		{'tweetText':tweet.full_text,
# 		'Date':createdAt,
# 		'authorName': tweet.author.name,
# 		})
# #dump the data into json format

# tweet_df = pd.DataFrame(tweetJson)

# tweet_df.to_csv(os.path.join(PATH_RESULT,str(ts)+'_'+'tweets.csv'), index=False)
# print(json.dumps(tweetJson))

# print(tweet_df)