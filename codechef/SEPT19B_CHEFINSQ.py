# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/10 21:25

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List



memo = {}
def combinations(n, r):
    if n < r:
        return 0

    if n == r or r == 0:
        return 1

    r = min(n-r, r)

    key = (n, r)
    if key in memo:
        return memo[key]

    ans = combinations(n-1, r) + combinations(n-1, r-1)
    memo[key] = ans

    return ans


T = int(input())
for ti in range(T):
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    A.sort()

    v = A[K-1]
    n = sum([1 if x == v else 0 for x in A])
    r = sum([1 if x == v else 0 for x in A[:K]])

    ans = combinations(n, r)
    print(ans)





