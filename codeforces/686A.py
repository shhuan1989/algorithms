# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/24 13:18

"""

N, X = map(int, input().split())

total = X
distres = 0
for i in range(N):
    o, v = input().split()
    v = int(v)
    if o == '+':
        total += v
    else:
        if total >= v:
            total -= v
        else:
            distres += 1

print(total, distres)