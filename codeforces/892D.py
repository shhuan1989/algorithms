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
created by shhuan at 2017/11/17 22:54

"""

N = int(input())

A = [int(x) for x in input().split()]

wc = collections.Counter(A)
if any(v > 1 for v in wc.values()):
    print(-1)
    exit(0)

C = list(sorted(A))

NC = {C[i]: C[i+1] for i in range(N-1)}
NC[C[-1]] = C[0]


ans = []
for v in A:
    ans.append(NC[v])

print(" ".join(map(str, ans)))