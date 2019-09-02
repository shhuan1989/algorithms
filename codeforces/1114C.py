# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2019/2/12 19:21


N! = N * (N-1) * (N-2) * ... * 2 * 1


"""


# 分解质因数
def decomp(val):
    d = 2
    ans = collections.defaultdict(int)
    while d <= math.sqrt(val):
        if val % d == 0:
            while val % d == 0:
                ans[d] += 1
                val //= d
        d += 1
    if val > 1:
        ans[val] += 1

    return ans

N, B = map(int, input().split())

comps = decomp(B)
ans = float('inf')
for y in comps.keys():
    z = y
    x = 0
    while z <= N:
        x += N // z
        z *= y
    ans = min(ans, x // comps[y])

print(ans)




