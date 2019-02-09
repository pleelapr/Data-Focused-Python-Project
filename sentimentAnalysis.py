import pandas as pd
import csv
import os
import re
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

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

tweets = pd.DataFrame()

for filename in os.listdir(PATH_RESULT):
	data = pd.read_csv(PATH_RESULT+'/'+filename)
	# print(data)
	tweets = tweets.append(data)

# print(tweets[0:6])

#Clean 
for i in range(len(tweets)):
	tweets.loc[i,'tweetText'] = clean_tweet(tweets.loc[i,'tweetText'])
	tweets.loc[i,'sentiment']= get_tweet_sentiment(tweets.loc[i,'tweetText'])

# print(tweets[0:6])

# picking positive tweets from tweets 
tweets_sentiment = tweets.groupby('sentiment').count()
print(tweets_sentiment)
