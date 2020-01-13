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
created by shhuan at 2020/1/10 22:02

"""


def solve(X):
    PX = X
    SX = int(math.sqrt(X))
    MAXN = SX + 1000
    p = [True for _ in range(MAXN)]
    p[0] = p[1] = False
    for i in range(MAXN):
        if p[i]:
            v = i + i
            while v < MAXN:
                p[v] = False
                v += i
    p = [i for i in range(MAXN) if p[i]]

    Y = []
    for u in p:
        if u > X:
            break
        if X % u == 0:
            c = 0
            while X % u == 0:
                c += 1
                X //= u
            Y.append(u ** c)
    if X > 1:
        Y.append(X)

    if not Y:
        return [1, 1]
    if len(Y) == 1:
        return [Y[0], 1]

    q = {1}
    for y in Y:
        q = {v * y for v in q if v * y <= SX} | q

    u = max(q)
    v = PX // u
    return [u, v]

    # NY = len(Y)
    # dp = [[0 for _ in range(SX+1)] for _ in range(NY)]
    #
    # for i, y in Y:
    #         dp[i][v] = max(dp[i-1][v], dp[i-1][v-y] + y)



X= int(input())
a, b = solve(X)
print('{} {}'.format(a, b))