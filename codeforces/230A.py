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
created by shhuan at 2017/11/22 10:14

"""

S, N = map(int, input().split())

xy = []
for i in range(N):
    x, y = map(int, input().split())
    xy.append((x, y))

xy.sort()

for x, y in xy:
    if S > x:
        S += y
    else:
        print("NO")
        exit(0)
print("YES")