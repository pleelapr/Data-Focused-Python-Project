import pandas as pd
import csv
import os
import re
import datetime
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer


PATH_RESULT = 'result'

#From different project
def clean_tweet(tweet):
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def vectorizer(tweets):
	cv = CountVectorizer(binary=True)
	cv.fit(tweets)
	tweets = cv.transform(tweets)
	return tweets

def get_tweet_sentiment(tweet):
	# create TextBlob object of passed tweet text 
	analysis = TextBlob(clean_tweet(tweet))
    # set sentiment 
	if analysis.sentiment.polarity > 0:
		return 'positive'
	elif analysis.sentiment.polarity == 0:
		return 'neutral'
	else: 
		return 'negative'

def get_tweets():
	tweets = pd.DataFrame()

	for filename in os.listdir(PATH_RESULT):
		data = pd.read_csv(PATH_RESULT+'/'+filename)
		# print(data)
		tweets = tweets.append(data)

	tweets.drop_duplicates(inplace=True)

	#Clean 
	for i in range(len(tweets)):
		tweets.loc[i,'tweetText'] = clean_tweet(tweets.loc[i,'tweetText'])
		tweets.loc[i,'sentiment']= get_tweet_sentiment(tweets.loc[i,'tweetText'])
	tweets['Date'] = tweets['Date'].str.slice(0, 10)
	tweets['Date'] = pd.to_datetime(tweets['Date'])
	print(tweets['Date'])
	return tweets

def main():
	# get each sentiment number
	tweets_sentiment = tweets['sentiment'].value_counts()
	print(tweets_sentiment)

