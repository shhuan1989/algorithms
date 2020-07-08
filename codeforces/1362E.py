# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/5

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


from functools import lru_cache


MOD = 10**9 + 7

@lru_cache(maxsize=None)
def pow(a, b):
    if a == 0:
        return 0
    if b == 0:
        return 1
    if b == 1:
        return a
    
    h = pow(a, b//2)
    res = h * h if b % 2 == 0 else h * h * a
    
    return res % MOD


def solve(P, K):
    if P == 1:
        return 1 if len(K) % 2 == 1 else 0
    
    INF = 10**6 + 100
    prevk = 10**6 + 10
    cursum = 0
    isinf = False
    ans = 0
    q = list(sorted(K))
    while q:
        k = q.pop()
        delta = prevk - k
        prevk = k
        
        ans *= pow(P, delta)
        ans %= MOD
        
        # cursum *= pow(P, delta)
        for i in range(min(delta, 20)):
            cursum *= P
            if cursum > INF:
                isinf = True
        
        while q and q[-1] == k:
            q.pop()
            if isinf or cursum > 0:
                cursum -= 1
                ans += MOD-1
            else:
                cursum +=  1
                ans += 1
            ans %= MOD
    
    ans *= pow(P, prevk)
    ans *= MOD
    
    return ans


T = int(input())
ans = []
for ti in range(T):
    N, P = map(int, input().split())
    K = [int(x) for x in input().split()]
    ans.append(solve(P, K))
    
print('\n'.join(map(str, ans)))