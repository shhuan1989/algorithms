# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/2/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

N = int(input())
A = [int(x) for x in input().split()]
M = int(input())
Q = []
MAXV = max(A) + 1

primes = []
count = [0] * MAXV
for v in A:
    count[v] += 1

NP = 10**6
ft = [0] * NP


def add(idx, val):
    while idx < NP:
        ft[idx] += val
        idx |= idx + 1


def query_imp(r):
    v = 0
    while r >= 0:
        v += ft[r]
        r = (r & (r+1)) - 1
    return v


def query(l, r):
    return query_imp(r) - query_imp(l-1)

fi = 0
P = [True] * MAXV
for i in range(2, MAXV):
    if P[i]:
        primes.append(i)
        u = i
        c = 0
        while u < MAXV:
            P[u] = False
            c += count[u]
            u += i
            
        add(fi, c)
        fi += 1

ans = []
for mi in range(M):
    l, r = map(int, input().split())
    i = bisect.bisect_left(primes, l)
    if i >= len(primes):
        ans.append(0)
        continue
    if primes[i] < l:
        i += 1
    j = bisect.bisect_right(primes, r)
    ans.append(query(i, j-1))
    

print('\n'.join(map(str, ans)))
