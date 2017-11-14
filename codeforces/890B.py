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
created by shhuan at 2017/11/12 23:56

"""

N = int(input())
A = [int(x) for x in input().split()]


vis = {}

for i in range(N-1, -1, -1):
    v = A[i]
    if v not in vis:
        vis[v] = N-i

mx = 0
ans = -1

for k, v in vis.items():
    if v > mx:
        mx = v
        ans = k

print(k)