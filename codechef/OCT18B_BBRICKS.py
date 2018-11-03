# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/1/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from functools import reduce
import operator as op

MOD = 10**9 + 7

def ncr(n, m):
    if m > n:
        return 0

    numer = reduce(op.mul, range(n, n - m, -1), 1)
    denom = reduce(op.mul, range(1, m + 1), 1)
    
    return numer // denom

def solve(N, K):
    if N < K:
        return 0
    
    ans = 0
    
    for x in range(K):
        t = ncr(K-1, x)
        t *= 2**(x+1)
        t %= MOD
        t *= ncr(N-K+1, x+1)
        t %= MOD
        ans += t
        ans %= MOD
    
    return ans

T = int(input())
for ti in range(T):
    N, K = map(int, input().split())
    print(solve(N, K))

# t0 = time.time()
# for i in range(5):
#     print(solve(random.randint(10**8, 10**9), 1000))
# print(time.time() - t0)
