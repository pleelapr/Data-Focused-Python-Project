# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 13:59:14 2019

@author: srimank95
"""
import datetime
import os
import pandas as pd
import re
from urllib.request import urlopen  
from bs4 import BeautifulSoup

EXPORT_PATH = 'stock_data'
date = datetime.datetime.now()

html = urlopen('https://finance.yahoo.com/'
               'quote/AAPL/history?p=AAPL')


aapl_daily_prices = BeautifulSoup(html.read(), "lxml")

fout = open('aapl_daily_prices_temp.txt', 'wt',
		encoding='utf-8')

fout.write(str(aapl_daily_prices))

fout.close()

# print the first table
# print(str(aapl_daily_prices.table))
# ... not the one we want

# so get a list of all table tags
table_list = aapl_daily_prices.findAll('table')

# how many are there?
# print('there are', len(table_list), 'table tags')

# look at the first 50 chars of each table
# for t in table_list:
#     print(str(t)[:100])

# only one class="t-chart" table, so add that
# to findAll as a dictionary attribute
tc_table_list = aapl_daily_prices.findAll('table',
                                          { "class" : "W(100%) M(0)" } )

# how many are there?
# print(len(tc_table_list), 'tables')

tc_table = tc_table_list[0]

# for c in tc_table.children:
#     print(str(c)[:200])
contents_list = []
# tag tr means table row, containing table data
# what are the children of those rows?
for c in tc_table.children:
    for r in c.children:
        #print(str(r)[:500])
        for i in r.children:
            # print(type(i.contents))
            # print(str(i.contents).strip()[:150])
            contents_list.append(str(i.contents).strip()[:150])
            #if (str(i.contents).strip()[:9]) != '[<strong':
            #    print(i.contents)
                #temp_data += i.contents
                #for m in i.children:
                 #   print(m.contents)

cleaned_div_list = []

for i in range(len(contents_list)):
    content = contents_list[i]
    if i < len(contents_list)-1:
        next_content = contents_list[i+1]
        if '[<strong' in next_content:
            continue
    if '[<strong' in content:
        continue
    else:
        idx = content.find('>')
        content = content[idx+1:]
        cleaned_div_list.append(content.replace('</span>]',''))

# for i in cleaned_div_list:
    # print(i)
            



## Get daily apple stock prices
appl = []
for c in tc_table.children:
    for r in c.children:
        for i in r.children:
            if str(i.contents).strip()[:8] != '[<strong': # or str(i.contents).strip()[3:8] != "[Close":
                #print(i.contents)
                for m in i.children:
                    # print(m.contents)
                    appl += [m.contents]


## Remove bad entries that are not real stock values
for i in appl:
    #print(str(i).strip()[3:8])
    if str(i).strip()[3:8] == "Close" or str(i).strip()[3:8] == 'pan d':
        appl.remove(i)

## Remove dates that occur twice because of the "dividend" row
appl_temp = []

for i in range(len(appl)):
    #print(str(i)[:5])
    if (str(appl[i])[2:5] + str(appl[i])[10:]) != (str(appl[i-1])[2:5] + str(appl[i-1])[10:]):
        # print(appl[i-1])
        appl_temp += [appl[i-1]]
    
"""
for i in range(len(appl)):
    print(appl[i], appl[i+7])
    if appl[i] == appl[i + 7]:
        appl.remove(i)
"""

## current day prices
current_day = []

appl_clean = []

## append column headers and each row of daily yields as a list to daily_yield_curves
for val in cleaned_div_list:
    # print(val)
    current_day += [val]
    # print(current_day)
    if len(current_day) == 7:
        appl_clean += [current_day]
        current_day = []

result_data = pd.DataFrame(appl_clean)
result_data.columns = result_data.iloc[0]
result_data = result_data.drop(0)
# result_data.reindex(result_data.index.drop(0))

result_data.to_csv(os.path.join(EXPORT_PATH,str(date.strftime("%Y-%m-%d-%H-%M-%S"))+'_'+'stock_data.csv'), index=False)


print(result_data)

