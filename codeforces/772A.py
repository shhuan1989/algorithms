# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/7/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, P, A, B):
    if P >= sum(A):
        return -1
    
    def check(t):
        return P*t >= sum([max(0, t*A[i]-B[i]) for i in range(N)])
    
    lo, hi = 0.0, 1e18
    while abs(hi - lo) > 1e-6:
        m = (lo + hi) / 2
        # print(lo, hi)
        if check(m):
            lo = m
        else:
            hi = m
    
    if hi > 1e18-100:
        return -1
    
    return lo


N, P = map(int, input().split())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    
print(solve(N, P, A, B))