# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/11

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

import matplotlib

import pandas as pd
import json

matplotlib.use('MacOSX')

df = pd.read_csv('~/Downloads/table.csv')
data = []
# print(df.head())
for i, row in df.iterrows():
    val = json.loads(row['Error Message'])
    token = val['tokenLength']
    userId = val.get('userId', 'NULL')
    place = val['place']
    count = row['Java Script Errors']
    for i in range(count):
        data.append((userId, token, place))
    
df = pd.DataFrame(columns=[ 'user id', 'token length', 'place'], data=data)
# print(pd.pivot_table(df, columns=['token length']))


wc = collections.Counter(df[df['place']=='receiver']['token length'].tolist())
wc = [(c, w) for w, c in wc.items()]
wc.sort(reverse=True)
print('\n'.join(['{} {}'.format(w, c) for c, w in wc]))

import matplotlib.pyplot as plt

wc = [(w, c) for c, w in wc]
wc.sort()
# plt.pie([c for w, c in wc], [w for w,c in wc])
# plt.show()

fig1, ax1 = plt.subplots()
ax1.pie([c for w, c in wc],labels=[w for w,c in wc], autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

plt.figure()
places = df['place'].tolist()
pwc = collections.Counter(places)
plt.hist(places,  bins=2)
plt.title('receiver {} queue {}'.format(pwc['receiver'], pwc['queue']))
plt.show()
