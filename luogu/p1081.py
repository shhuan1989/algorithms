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
created by shhuan at 2020/7/12 15:19

"""''



if __name__ == '__main__':
    N = int(input())
    H = [int(x) for x in input().split()]
    X0 = int(input())
    A = []
    M = int(input())
    for i in range(M):
        x, s = map(int, input().split())
        A.append((x, s))

    hi = [-1 for _ in range(N)]
    pre = [-1 for _ in range(N)]
    after = [-1 for _ in range(N)]
    h = [(v, i) for i, v in enumerate(H)]
    h.sort()

    for i, (v, j) in enumerate(h):
        hi[j] = i
        pre[j] = i-1
        after[j] = i + 1 if i + 1 < N else -1

    toa = [-1 for _ in range(N+1)]
    toad = [float('-inf') for _ in range(N+1)]
    tob = [-1 for _ in range(N+1)]
    tobd = [float('-inf') for _ in range(N + 1)]
    for i in range(N):
        # a, b, c, d, e
        c = H[i]
        neibs = []
        if pre[i] >= 0:
            a = h[pre[i]][1]
            neibs.append(a)
            if pre[a] >= 0:
                b = h[pre[a]][1]
                neibs.append(b)
        if after[i] >= 0:
            d = h[after[i]][1]
            neibs.append(d)
            if after[d] >= 0:
                e = h[after[d]][1]
                neibs.append(e)
        if not neibs:
            continue

        f = [(abs(c-H[j]), H[j], j) for j in neibs]
        f.sort()

        if len(f) > 1:
            toa[i] = f[1][2]
            toad[i] = f[1][0]
        if len(f) > 0:
            tob[i] = f[0][2]
            tobd[i] = f[0][0]

        if pre[i] >= 0:
            after[h[pre[i]][1]] = after[i]
        if after[i] >= 0:
            pre[h[after[i]][1]] = pre[i]



    K = 1
    while 2 ** K <= N:
        K += 1

    TO = [[-1 for _ in range(K)] for _ in range(N)]
    TOD = [[float('-inf') for _ in range(K)] for _ in range(N)]
    TOAD = [[float('-inf') for _ in range(K)] for _ in range(N)]
    TOBD = [[float('-inf') for _ in range(K)] for _ in range(N)]

    for i in range(N-1, -1, -1):
        TO[i][0] = tob[toa[i]]
        TOD[i][0] = toad[i] + tobd[toa[i]]
        TOAD[i][0] = toad[i]
        TOBD[i][0] = tobd[toa[i]]
        for k in range(1, K):
            if TO[i][k-1] < 0:
                break
            TO[i][k] = TO[TO[i][k-1]][k-1]
            TOD[i][k] = TOD[TO[i][k-1]][k-1] + TOD[i][k-1]
            TOAD[i][k] = TOAD[i][k-1] + TOAD[TO[i][k-1]][k-1]
            TOBD[i][k] = TOBD[i][k-1] + TOBD[TO[i][k-1]][k-1]


    def query(start, dist):
        if start >= N:
            return 0, 0, 0, 0

        da, db = 0, 0
        while dist >= 0:
            k = 0
            while k < K and 0 <= TOD[start][k] <= dist:
                k += 1
            k -= 1
            if k < 0:
                return start, dist, da, db

            da += TOAD[start][k]
            db += TOBD[start][k]
            dist -= TOD[start][k]
            start = TO[start][k]


        return start, dist, da, db



    # question 1
    INF = 10**9+7
    avsb = INF
    s0 = -1
    for i in range(N):
        s, d, da, db = query(i, X0)
        if 0 <= toad[s] <= d:
            da += toad[s]
            d -= toad[s]
            s = toa[s]
        nab = da/db if db > 0 else INF
        if nab < avsb:
            avsb = nab
            s0 = i + 1

    print(s0)

    # question 2

    for x, s in A:
        s, d, da, db = query(x-1, s)
        if s < N and 0 <= toad[s] <= d:
            da += toad[s]
        print('{} {}'.format(da, db))

