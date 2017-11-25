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
created by shhuan at 2017/11/24 17:30

"""


N = int(input())

A = [int(x) for x in input().split()]


presum = [0] *(N+1)

for i in range(1, N+1):
    presum[i] = presum[i-1] + A[i-1]

if presum[-1] % 3 != 0:
    print(0)
    exit(0)

a = presum[-1] // 3
b = presum[-1] * 2 // 3
c = presum[-1]

idx = collections.defaultdict(list)

for i in range(1, N+1):
    if presum[i] == a:
        idx[a].append(i)
    elif presum[i] == b:
        idx[b].append(i)
    elif presum[i] == c:
        idx[c].append(i)

ans = 0
for i in idx[a]:
    l = bisect.bisect_right(idx[b], i)
    r = bisect.bisect_left(idx[b], N)
    ans += max(0, r-l)

print(ans)


