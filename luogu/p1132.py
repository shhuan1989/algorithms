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
created by shhuan at 2020/7/18 12:30

"""

def tonum(a):
    v = 0
    for u in a:
        v *= 10
        v += u

    return v


def numlen(val):
    n = 0
    while val > 0:
        n += 1
        val //= 10

    return n

def expand(u):
    digits = []
    while u > 0:
        digits.append(u % 10)
        u //= 10
    digits = digits[::-1]

    ans = set()
    # swap
    nd = len(digits)
    for i in range(nd):
        for j in range(i+1, nd):
            w = digits.copy()
            w[i], w[j] = w[j], w[i]
            ans.add(tonum(w))
    # delete
    for i in range(nd):
        w = digits.copy()
        w = w[:i] + w[i+1:]
        ans.add(tonum(w))

    # insert
    for i in range(nd-1):
        for v in range(digits[i]+1, digits[i+1]):
            w = digits.copy()
            w.insert(i+1, v)
            ans.add(tonum(w))

    return ans


if __name__ == '__main__':
    S = int(input())
    NS = numlen(S)
    INF = 10**9 + 7
    MAXN = 10**6
    dist = [INF for _ in range(MAXN)]

    q = [S]
    dist[S] = 0
    while q:
        nq = []
        for u in q:
            for v in expand(u):
                if numlen(v) <= NS and dist[v] >= INF:
                    dist[v] = dist[u] + 1
                    nq.append(v)
        q = nq


    # for d in range(1, INF):
    #     q = []
    #     for v in range(1, MAXN):
    #         if dist[v] == d:
    #             q.append(v)
    #     if not q:
    #         break
    #     print(d, q)


    M = int(input())
    ans = []
    for i in range(M):
        v = int(input())
        ans.append(dist[v] if dist[v] < INF else -1)

    print('\n'.join(map(str, ans)))



