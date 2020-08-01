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
created by shhuan at 2020/7/27 19:45

"""

MAXN = 10**3
isprimes = [True for _ in range(MAXN)]
isprimes[0] = False
isprimes[1] = False

for i in range(2, MAXN):
    if isprimes[i]:
        u = i + i
        while u < MAXN:
            isprimes[u] = False
            u += i

primes = [i for i in range(2, MAXN) if isprimes[i]][:21]


def brutal(l, r):
    maxc, maxv = 0, 0
    for u in range(l, r+1):
        v = u
        wc = collections.defaultdict(int)
        i = 2
        while i * i <= v:
            while v % i == 0:
                v //= i
                wc[i] += 1
            i += 1
        if v > 1:
            wc[v] += 1
        cnt = 1
        for c in wc.values():
            cnt *= c + 1
        if cnt > maxc:
            maxc = cnt
            maxv = u

    return maxc, maxv




if __name__ == '__main__':
    L, R = map(int, input().strip().split())

    np = len(primes)
    pows = [0 for _ in range(np)]
    def dfs(index, prec, prev, prep):
        if index >= np:
            # print(prev, prec, ps)
            return (prec, prev) if L <= prev <= R else (0, 0)
        if prev > R:
            return 0, 0

        ansc = prec
        ansv = prev
        b = primes[index]
        for p in range(prep+1):
            w = prev * (b ** p)
            if w > R:
                break

            nc, nv = dfs(index+1, prec * (p+1), w, p)
            if L <= nv <= R:
                if nc > ansc:
                    ansc = nc
                    ansv = nv
                elif nc == ansc and nv < ansv:
                    ansv = nv

        return (ansc, ansv) if L <= ansv <= R else (0, 0)

    c, v = dfs(0, 1, 1, 10000) if R-L > 100000 else brutal(L, R)
    # print(c, v)

    print('Between {} and {}, {} has a maximum of {} divisors.'.format(L, R, v, c))


