# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


MAXN = 129
A = [0] * MAXN
lasti = [[] for _ in range(MAXN)]
lasti[0].append(1)

for i in range(2, MAXN):
    v = A[i-1]
    if len(lasti[v]) < 2:
        lasti[0].append(i)
        continue
    A[i] = lasti[v][-1] - lasti[v][-2]
    lasti[A[i]].append(i)
    

T = int(input())
for ti in range(T):
    N = int(input())
    ans = sum([1 if v == A[N] else 0 for v in A[1: N+1]] or [0])
    print(ans)
