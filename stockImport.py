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

def get_stock_csv():
	#Get Stock Detail
	stock_detail = pd.read_csv(EXPORT_PATH+'/'+'APPL best.csv')
	# cols = stock_detail.columns
	stock_detail.drop_duplicates(inplace=True)

	stock_detail.reset_index(inplace=True)
	# print(stock_detail['Adj. Close'])
	stock_result = pd.DataFrame()

	stock_result['Date'] = pd.to_datetime(stock_detail.Dates.astype(str), errors='coerce')
	stock_result['BEST_TARGET_PRICE'] = pd.to_numeric(stock_detail.BEST_TARGET_PRICE, errors='coerce')
	# stock_result['PX_LAST'] = pd.to_numeric(stock_detail.PX_LAST, errors='coerce')

	stock_result['Date'] = pd.to_datetime(stock_result['Date'])

	#Export Stock Data to CSV
	# stock_incr_decr.to_csv(os.path.join(EXPORT_PATH,str(end)+stock_name+'_'+'stock_result.csv'), index=False)

	return stock_result

def get_stock_quandl():
	#Get Stock Detail
	stock_detail = quandl.get("WIKI/" + stock_name, start_date=start, end_date=end)
	# cols = stock_detail.columns
	# stock_detail['Adj. Close'] = (stock_detail[cols] == 'Adj. Close').astype(float).sum(axis=1)

	stock_detail.reset_index(inplace=True)
	# print(stock_detail['Adj. Close'])

	stock_incr_decr = pd.DataFrame()

	for i in range(len(stock_detail)):
		# print(stock_detail['Adj. Close'].iloc[0])
		if i == 0:
			continue
		else:
			previous_index = i-1
			indicator = stock_detail['Adj. Close'].iloc[i] - stock_detail['Adj. Close'].iloc[previous_index]
			if indicator > 0:
				#The Adj. Close is increased
				result = 1
			else:
				#The Adj. Close is not increased
				result = 0
			# print(stock_detail['Date'].iloc[i])
			# print(result)
			df = pd.DataFrame(data=[[stock_detail['Date'].iloc[i], result]],columns=['Date','result'])
			stock_incr_decr = stock_incr_decr.append(df)

	stock_incr_decr['Date'] = pd.to_datetime(stock_incr_decr['Date'])
	#Export Stock Data to CSV
	# stock_incr_decr.to_csv(os.path.join(EXPORT_PATH,str(end)+stock_name+'_'+'stock_result.csv'), index=False)
	return stock_incr_decr