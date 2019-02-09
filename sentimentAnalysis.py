import pandas as pd
import csv
import os
import re

PATH_RESULT = 'result'

def clean_tweet(tweet): 
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

tweets = pd.DataFrame()
for filename in os.listdir(PATH_RESULT):
	data = pd.read_csv(PATH_RESULT+'/'+filename)
	# print(data)
	tweets = tweets.append(data)

print(tweets[0:6])

for i in range(len(tweets)):
	tweets.loc[i,'tweetText'] = clean_tweet(tweets.loc[i,'tweetText'])

print(tweets[0:6])