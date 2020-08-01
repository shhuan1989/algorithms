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
created by shhuan at 2020/7/20 21:18

"""


if __name__ == '__main__':
    N = int(input())

    MAXN = 10**5+5
    LIST = [0, 1] + [-1 for _ in range(MAXN)]
    PRE = [-1, -1] + [-1 for _ in range(MAXN)]
    AFTER = [-1, -1] + [-1 for _ in range(MAXN)]

    for i in range(N-1):
        u = i + 2
        w, v = map(int, input().split())
        LIST[u] = u

        if v == 0:
            PRE[u] = PRE[w]
            AFTER[PRE[w]] = u
            PRE[w] = u
            AFTER[u] = w
        else:
            AFTER[u] = AFTER[w]
            PRE[AFTER[w]] = u
            AFTER[w] = u
            PRE[u] = w

    M = int(input())
    for i in range(M):
        u = int(input())
        if LIST[u] < 0:
            continue
        LIST[u] = -1
        if PRE[u] > 0:
            AFTER[PRE[u]] = AFTER[u]
        if AFTER[u] > 0:
            PRE[AFTER[u]] = PRE[u]
        PRE[u] = -1
        AFTER[u] = -1

    for i in range(1, N+1):
        if LIST[i] > 0 and PRE[i] < 0:
            ans = []
            u = i
            while u > 0:
                ans.append(u)
                u = AFTER[u]
            print(' '.join(map(str, ans)))
            exit(0)








