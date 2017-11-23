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
created by shhuan at 2017/11/23 10:33

"""


N = int(input())

B = [int(x) for x in input().split()]


maxb, maxbcount, minb, minbcount = float('-inf'), 0, float('inf'), 0

for b in B:
    if b > maxb:
        maxb = b
        maxbcount = 1
    elif b == maxb:
        maxbcount += 1

    if b < minb:
        minb = b
        minbcount = 1
    elif b == minb:
        minbcount += 1

if maxb == minb:
    print(0, maxbcount * (maxbcount-1) // 2)
else:
    print(maxb-minb, maxbcount * minbcount)

