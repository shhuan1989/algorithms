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

import numpy as np

versions = [('2.7.3', 10), ('2.26.2', 90)]


def getVersion():
    
    probs = [p for v, p in versions]
    s = sum(probs)
    probs = [p/s for p in probs]
    
    vs = [v for v, p in versions]
    
    return np.random.choice(vs, p=probs)


def getDuration():
    return np.random.normal(100, 50)
    

data = []
uc = [1000, 100] * 1000

for t in range(1000):
    for user in range(uc[t]):
        v = getVersion()
        d = int(getDuration())
        data.append((v, d+t))
        
x0 = [0 for i in range(1200)]
x1 = [0 for i in range(1200)]
for v, t in data:
    if t >= 1200:
        continue
    if v == '2.26.2':
        x0[t] += 1
    else:
        x1[t] += 1


import matplotlib.pyplot as plt

plt.plot(x0, label='2.26.2')
plt.plot(x1, label='2.27.3')
plt.legend()
plt.show()

