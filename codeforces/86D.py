# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/1/1 15:50

"""


N, T = map(int, input().split())
M = max(int(math.sqrt(N)), 1)
A = [int(x) for x in input().split()]
Q = []
for i in range(T):
    l, r = map(int, input().split())
    l -= 1
    Q.append((l//M, l, r//M,
              r, i))

P = []
for i in range(0, N, M):
    wc = collections.defaultdict(int)
    for j in range(i, min(N, i+M)):
        wc[A[j]] += 1

Q.sort()

ans = [0 for _ in range(T)]
p = -1
s = 0
pwc = collections.defaultdict(int)
for qi, (pl, l, pr, r, i) in enumerate(Q):
    if pl == pr:
        pwc = collections.defaultdict(int)
        for j in range(l, r):
            pwc[A[j]] += 1
        s = sum([c**2*w for w, c in pwc.items()])
        ans[i] = s
    elif p == pl and Q[qi-1][0] != Q[qi-1][2]:
        for j in range(Q[qi-1][1], l):
            pwc[A[j]] -= 1

        if Q[qi-1][1] == pr:
            for j in range(Q[qi-1][3], r):
                pwc[A[j]] +=
        else:
            for j in range(Q[qi-1][1] * M, Q[qi-1][3]):
                pwc[A[j]] -= 1
            for j in range(Q[qi-1][1], pr):
                u = P[j]
                for w, c in u.items():
                    pwc[w] += c
            for j in range(pr*M, r):
                pwc[A[j]] += 1

        s = sum([c**2*w for w, c in pwc.items()])
        ans[i] = s
    else:
        p = pl
        wc = collections.defaultdict(int)
        for j in range(p, pr):
            u = P[j]
            for w, c in u.items():
                wc[w] += c
        for j in range(pl * M, l):
            wc[A[j]] -= 1
        for j in range(pr*M, r):
            wc[A[j]] += 1
        s = sum([c**2*w for w, c in wc.items()])
        ans[i] = s
        pwc = wc

print('\n'.join(map(str, ans)))
