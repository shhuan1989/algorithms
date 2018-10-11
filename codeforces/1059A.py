# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/10/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

N, L, A = map(int, input().split())

res = 0
rest = 0
for i in range(N):
    t, l = map(int, input().split())
    
    res += (t-rest) // A
    rest = t+l

res += (L-rest) // A

print(res)
