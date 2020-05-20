import math
import os
import random
import re
import sys
from typing import List
import bisect
import collections
import heapq



def cal(x):
    y = x // 12
    
    if y < 3000:
        return x - x * 0.03
    elif y < 12000:
        return x - x * 0.1 - 210
    elif y < 25000:
        return x - x * 0.2 - 1410
    elif y < 35000:
        return x - x * 0.25 - 2660
    elif y < 55000:
        return x - x * 0.3 - 4410
    elif y < 80000:
        return x - x * 0.35 - 7160
    else:
        return x - x * 0.45 - 15160
    
    
import matplotlib.pyplot as plt

x = [i for i in range(1, 200000)]
y = [cal(v) for v in x]
plt.plot(x, y)
plt.show()

print(cal(160000))
print(cal(140000))
