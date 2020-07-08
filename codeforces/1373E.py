# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/29

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def check(n, s, t, k):
    sm = 0
    
    for i in range(s, min(s+k+1, 10)):
        sm += 9 * n + i
    if s + k > 9:
        for i in range((s+k)%10+1):
            sm += 1 + i
    
    d = t - sm
    if d < 0:
        return False, -1
    
    k += 1
    if d % k == 0:
        d //= k
        prefix = ''
        pv = 8
        while d > 0:
            c = min(d, pv)
            prefix += str(c)
            d -= c
            pv = 9
        
        return True, int(prefix[::-1] + '9' * n + str(s))
    
    return False, -1


def solve(N, K):
    ans = float('inf')
    for i in range(N//9+1):
        for s in range(10):
            c, v = check(i, s, N, K)
            if c:
                ans = min(ans, v)
    
    return ans if ans < float('inf') else -1


T = int(input())
for ti in range(T):
    N, K = map(int, input().split())
    print(solve(N, K))

