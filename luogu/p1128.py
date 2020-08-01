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
created by shhuan at 2020/7/18 19:32

"""

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

NP = len(primes)
ANSV = [float('inf')]
ANSP = [0 for _ in range(NP)]
TMP = [0 for _ in range(NP)]
LOG = [0.0 for _ in range(NP)]
for i in range(NP):
    LOG[i] = math.log(primes[i], 10)


def dfs(logv, rest, pi):
    if logv >= ANSV[0]:
        return

    if rest == 1:
        # print(logv)
        for i in range(pi):
            ANSP[i] = TMP[i]
        for i in range(pi, NP):
            ANSP[i] = 0
        ANSV[0] = min(ANSV[0], logv)
        # print(ANSP)
        return

    if pi >= N:
        return

    i = 1
    while i**2 <= rest:
        if rest % i == 0:
            j = i-1
            if i != 1:
                TMP[pi] = j
                dfs(logv + LOG[pi] * j, rest//i, pi + 1)
            if i**2 != rest:
                TMP[pi] = rest//i-1
                dfs(logv + LOG[pi] * TMP[pi], i, pi + 1)
        i += 1

if __name__ == '__main__':
    N = int(input())

    dfs(0, N, 0)
    ans = 1
    for i in range(NP):
        ans *= primes[i] ** ANSP[i]
    print(ans)







