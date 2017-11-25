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
created by shhuan at 2017/11/24 18:49

"""


N = int(input())

S = input()

count = [0] * 10

for v in [int(v) for v in S]:
    if v == 4:
        count[3] += 1
        count[2] += 2
    elif v == 8:
        count[2] += 3
        count[7] += 1
    elif v == 6:
        count[5] += 1
        count[3] += 1
    elif v == 9:
        count[2] += 1
        count[3] += 2
        count[7] += 1
    else:
        count[v] += 1

ans = ""
for i in range(9, 1, -1):
    ans += str(i) * count[i]
print(ans)