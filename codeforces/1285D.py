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

def blen(v):
    s = 0
    while v > 0:
        s += 1
        v >>= 1
    return s


def solve(A):
    def dfs(index, pre, vals):
        if not vals:
            return float('inf')
        if index < 0:
            return max([pre ^ v for v in vals])

        bv = 1 << index
        a = [v for v in vals if v & bv > 0]

        if not a:
            return dfs(index-1, pre, vals)
        elif len(a) == len(vals):
            return dfs(index-1, pre | bv, a)
        else:
            b = [v for v in vals if v & bv == 0]
            return min(dfs(index-1, pre | bv, b), dfs(index-1, pre, a))

    N = max([blen(v) for v in A])
    return dfs(N-1, 0, A)


# N = int(input())
# A = [int(x) for x in input().split()]
# print(solve(A))
t0 = time.time()
print(solve([random.randint(1, 2**30) for _ in range(10**5)]))
print(time.time() - t0)