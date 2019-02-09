import pandas as pd
import csv
import os

PATH_RESULT = 'result'

def clean_tweet(tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

tweets = pd.DataFrame()
for filename in os.listdir(PATH_RESULT):
	data = pd.read_csv(PATH_RESULT+'/'+filename)
	print(data)
	tweets.append(data)

print(tweets[0:6])

