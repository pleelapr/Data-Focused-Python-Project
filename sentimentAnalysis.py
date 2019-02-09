import pandas as pd
import csv
import os
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

PATH_RESULT = 'result'

#From different project
def clean_tweet(tweet): 
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def vectorizer(tweet):
	cv = CountVectorizer(binary=True)
	cv.fit(reviews_train_clean)
	X = cv.transform(reviews_train_clean)
	X_test = cv.transform(reviews_test_clean)

tweets = pd.DataFrame()

for filename in os.listdir(PATH_RESULT):
	data = pd.read_csv(PATH_RESULT+'/'+filename)
	# print(data)
	tweets = tweets.append(data)

# print(tweets[0:6])

#Clean 
for i in range(len(tweets)):
	tweets.loc[i,'tweetText'] = clean_tweet(tweets.loc[i,'tweetText'])

print(tweets[0:6])