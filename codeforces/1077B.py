# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/11/16 22:42

"""

N = int(input())

A = [int(x) for x in input().split()]


wc = collections.defaultdict(int)
for i in range(1, N-1):
    if A[i] == 0 and A[i-1] == A[i+1] == 1:
        wc[i-1] += 1
        wc[i+1] += 1

ans = 0
for k in [k for k, v in wc.items() if v > 1]:
    A[k] = 0
    ans += 1

for i in range(1, N-1):
    if A[i] == 0 and A[i-1] == A[i+1] == 1:
        ans += 1

print(ans)
