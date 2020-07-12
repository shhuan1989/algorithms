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
created by shhuan at 2020/7/10 20:02

"""

if __name__ == '__main__':
    MAXN = 150
    MAXL = 300 * 105
    stone = [0 for _ in range(MAXN)]
    A = [0 for _ in range(MAXN)]
    DP = [float('inf') for _ in range(MAXL)]
    VIS = [False for _ in range(MAXL)]
    L = int(input())
    S, T, M = map(int, input().split())
    base = S * T
    line = [int(x) for x in input().split()]
    line.sort()
    for i in range(1, M+1):
        stone[i] = line.pop(0)

    if S == T:
        ans = 0
        for i in range(1, M+1):
            if stone[i] % S == 0:
                ans += 1
        print(ans)
    else:
        for i in range(1, M+1):
            d = stone[i] - stone[i-1]
            if d >= base:
                d = base
            A[i] = A[i-1] + d
            VIS[A[i]] += 1

        L = A[M] + base
        DP[0] = 0
        for i in range(1, L+1):
            for j in range(S, T+1):
                if i - j >= 0:
                    if VIS[i]:
                        DP[i] = min(DP[i-j]+1, DP[i])
                    else:
                        DP[i] = min(DP[i-j], DP[i])

        ans = MAXN
        for i in range(A[M], L+1):
            ans = min(ans, DP[i])
        print(ans)




