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
created by shhuan at 2017/11/22 20:40

"""

M, S = map(int, input().split())

if S == 0:
    if M == 1:
        print(0, 0)
    else:
        print(-1, -1)
elif S < 0:
    print(-1, -1)
elif M * 9 < S:
    print(-1, -1)
else:

    maxVal = 0
    s = S
    for i in range(M):
        maxVal *= 10
        v = min(9, s)
        maxVal += v
        s -= v
    if s != 0:
        maxVal = -1

    minVal = 0
    s = S
    for i in range(M):
        minVal *= 10
        v = max(0, s - (M-i-1)*9)
        if i == 0:
            v = max(v, 1)
        minVal += v
        s -= v
    if s != 0:
        minVal = -1

    print(minVal, maxVal)







