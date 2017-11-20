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
created by shhuan at 2017/11/20 16:52

"""


def next_state(state, n):
    # 0 -> 0
    # 1 -> 0 | 1
    # 11 的数量成对出现
    ans = []
    for i in range(2**n):
        f = True
        c1 = 0
        for j in range(n):
            if (i >> j) & 1 == 1 and (state >> j) & 1 != 0:
                c1 += 1
            else:
                if c1 % 2 != 0:
                    f = False
                    break
                c1 = 0
            if (state >> j) & 1 == 0 and (i >> j) & 1 == 0:
                f = False
                break
        if f and c1 % 2 == 0:
            ans.append(i)

    return ans

while True:
    h, w = map(int, input().split())

    if h == 0 and w == 0:
        exit(0)

    N = 2**w
    dp = [[0 for _ in range(N)] for _ in range(h+1)]

    dp[0][N-1] = 1

    for r in range(1, h+1):
        for state in range(N):
            v = dp[r-1][state]
            if v != 0:
                # state => next_state
                ns = next_state(state, w)
                for s in ns:
                    dp[r][s] += v

    print(dp[h][N-1])
