from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import datetime
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import sentimentAnalysis as sa
import Apple_stock_scrape as ass
import stockImport as si

EXPORT_PATH = 'analysis_data'
date = datetime.datetime.now()


tweets_data = sa.get_tweets()
stock_data = si.get_stock_csv()
stock_data2 = ass.get_stock()

print(tweets_data[0:6])
print(stock_data[0:6])

print(tweets_data.columns)
tweets_data['Date'] = tweets_data['Date'].astype(str)
stock_data['Date'] = stock_data['Date'].astype(str)
stock_data2['Date'] = stock_data2['Date'].astype(str)

result_data = pd.merge(tweets_data, stock_data, how='left', left_on=['Date'], right_on=['Date'])
result_data = pd.merge(result_data, stock_data2, how='left', left_on=['Date'], right_on=['Date'])


result_data.to_csv(os.path.join(EXPORT_PATH,str(date.strftime("%Y-%m-%d-%H-%M-%S"))+'_'+'merge_data.csv'), index=False)

print(result_data[0:6])