#!/usr/bin/env python
# coding: utf-8

# In[21]:

import numpy as mp
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime
import json

#Question #1

a = [2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,
10,3,7,9,6,0,1,3,5,6,5,5,6,6,7,7,8,9,10,2,3,6,8,
9,10,6,7,4,3]

a.sort()
freq = {}
for i in a:
    count = 0
    if i in freq:
        count = freq[i] + 1
        freq.update({i: count})
    if i not in freq:
        count = 1 
        freq.update({i: count})
print(freq)
plt.hist(a, bins = 11)
plt.title('Histogram')
plt.show()

with open('my_data.json', 'w', encoding='utf-8') as out:
    json.dump(freq, out, ensure_ascii = False, indent = 2)



# In[22]:

#Question #2
#Choice 2: How much have you spent on Amazon?

#Get the data
df = pd.read_csv('midterm_amz_data.csv')

#Check and clean the data
df.dropna(axis=1, how='any',inplace =True)
df = df.replace('\$','', regex = True)
df = df.replace('\/','-', regex = True)

#conver date data to datetime
for i,row in df.iterrows():
    order_date = df.loc[i, 'Order Date']
    order_date2 = datetime.strptime(order_date, '%m-%d-%Y')
    df.replace(order_date, order_date2)

#print(df.head(10))
    
#Price data analysis 
df['Purchase Price Per Unit'] = pd.to_numeric(df['Purchase Price Per Unit'], downcast="float")
price = (df['Purchase Price Per Unit'])


average_price = price.mean()
max_price = price.max()
min_price = price.min()
total_spent = price.sum()

count = 0
for i in df['Purchase Price Per Unit']:
    if i == max_price:
        max_item = df.loc[count, 'Title']
    if i == min_price:
        min_item = df.loc[count, 'Title']
    count += 1

print('Highest Price:', max_item, 'purchased at', "{:.2f}".format(max_price))
print('Lowest Price:', min_item, 'purchased at', "{:.2f}".format(min_price))
print()
print('Mean Price:', "{:.2f}".format(average_price))
print('Total Spent:', total_spent)
  
#Display data by date
df.plot(kind = 'bar', x = 'Order Date', y = 'Purchase Price Per Unit')
plt.title('Spending by Date')
plt.show()

#Display by date part two
df.groupby(['Order Date']).sum().plot(kind='line', y = 'Purchase Price Per Unit', figsize = (5,5))
plt.title('Monthly Spending Data')
plt.show()

#Display data by category
df.groupby(['Category']).sum().plot(kind='pie', y = 'Purchase Price Per Unit', figsize = (20,20))
plt.plot('Spending by Category')
plt.show()

