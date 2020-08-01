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
created by shhuan at 2020/7/28 18:46

"""



perm = [0, 1]
for i in range(2, 32):
    perm.append(perm[-1] * i)


def ncr(c, r):
    if c < r:
        return 0
    if c-r < r:
        return ncr(c, c-r)
    if r == 1:
        return c
    if r == 0:
        return 1

    return ncr(c-1, r) + ncr(c-1, r-1)

if __name__ == '__main__':
    N, K = map(int, input().split())

    ans = []
    def dfs(rest, k):
        if k <= 0:
            return

        n = len(rest)
        y = sum([ncr(n-1, i) * perm[i] for i in range(1, n)] or [0])

        # if y == k:
        #     for v in rest:
        #         ans.append(v)
        #     return

        for x in range(len(rest)+1):
            if x * y == k - 1:
                ans.append(rest[x])
                break
            elif x * y > k:
                ans.append(rest[x-1])
                dfs(rest[:x-1] + rest[x:], k-(x-1)*y-1)

    dfs([i for i in range(1, N+1)], K)
    print(' '.join(map(str, ans)))
