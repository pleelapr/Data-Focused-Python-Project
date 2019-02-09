import pandas as pd
import quandl
import datetime
import os

EXPORT_PATH = 'stock_data'

quandl.ApiConfig.api_key = "fZ_aBrDidHJs_hmhzGnT"

#Get the data from/to date
start = datetime.datetime(2016,1,1)
end = datetime.date.today()

#Defined Stock name
stock_name = "AAPL"

#Get Stock Detail
stock_detail = quandl.get("WIKI/" + stock_name, start_date=start, end_date=end)

print(stock_detail)

#Export Stock Data to CSV
stock_detail.to_csv(os.path.join(EXPORT_PATH,str(end)+stock_name+'_'+'stock.csv'), index=True)