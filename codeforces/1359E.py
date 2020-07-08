# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/4

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

from functools import lru_cache


MOD = 998244353

MAXN = 5*10**5 + 5

FAC = [1 for _ in range(MAXN)]

for i in range(1, MAXN):
    FAC[i] = (i * FAC[i-1]) % MOD
    

@lru_cache(maxsize=None)
def pow(x, y):
    if y == 0:
        return 1
    if x == 0:
        return 0
    if y == 1:
        return x
    
    a = pow(x, y//2)
    b = a * a if y % 2 == 0 else a * a * x
    
    return b % MOD


# (x * inv(x)) % P == 1
def inv(x):
    return pow(x, MOD-2)
    

# ncr(c, r) % MOD = n!//(r! * (c-r)!) % MOD = n! * (r! * (c-r)!)^(MOD-2) % MOD
def ncr(c, r):
    if r == 0:
        return 1
    if r == 1:
        return c
    if c < r:
        return 0
    if c == r:
        return 1
    
    return (FAC[c] * inv(FAC[r] * FAC[c-r])) % MOD



# @lru_cache(maxsize=None)
# def ncr(c, r):
#     if c < r:
#         return 0
#     if c == r:
#         return 1
#     if r == 0:
#         return 1
#
#     return ncr(c-1, r-1) + ncr(c-1, r)


def solve(N, K):
    if N < K:
        return 0
    if N == K:
        return 1
    if K == 1:
        return N
    
    ans = 0
    for minVal in range(1, N+1):
        t = N // minVal
        if t < K:
            break
        ans += ncr(t-1, K-1)
        ans %= MOD
    
    return ans


N, K = map(int, input().split())
print(solve(N, K))