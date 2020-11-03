# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/8 21:40

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

from functools import lru_cache
if __name__ == '__main__':
    N, M, S = map(int, input().strip().split())
    W, V = [], []
    for _ in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)

    A = []
    maxr = 0
    for _ in range(M):
        l, r = map(int, input().split())
        maxr = max(maxr, r-1)
        A.append((l-1, r-1))

    presum = [0 for _ in range(N+1)]
    precount = [0 for _ in range(N+1)]

    @lru_cache(maxsize=None)
    def get(weight):
        for i, w in enumerate(W):
            if i > maxr:
                break
            presum[i+1] = presum[i]
            precount[i+1] = precount[i]

            if w >= weight:
                presum[i+1] += V[i]
                precount[i+1] += 1

        x = 0
        for l, r in A:
            s = presum[r+1] - presum[l]
            c = precount[r+1] - precount[l]
            x += s * c

        return x

    weights = list(sorted(set(W)))
    lo, hi = 0, len(weights)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        v = get(weights[mid])
        if v == S:
            print(0)
            exit(0)
        elif v < S:
            hi = mid - 1
        else:
            lo = mid + 1

    ans = min([abs(get(weights[i])-S) for i in range(hi, min(lo+1, len(weights)))])
    print(ans)
