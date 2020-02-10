# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/15/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def check(val, A, M):
    s = set()
    for row in A:
        v = 0
        for u in row:
            v <<= 1
            if u >= val:
                v |= 1
        s.add(v)
    
    x = 1 << M
    for u in s:
        for v in range(x):
            if v in s and u | v == x - 1:
                return True
            
    return False


def getAnswer(val, A, M):
    vi = {}
    for i, row in enumerate(A):
        v = 0
        for u in row:
            v <<= 1
            if u >= val:
                v |= 1
        vi[v] = i
        
    x = 1 << M
    for u in vi:
        for v in range(x):
            if v in vi and u | v == x - 1:
                return vi[u], vi[v]
    
    return 0, 0


def solve(N, M, A):
    lo, hi = 0, max([max(row) for row in A])
    
    while lo <= hi:
        m = (lo + hi) // 2
        if check(m, A, M):
            lo = m + 1
        else:
            hi = m - 1
    
    a, b = getAnswer(hi, A, M)
    print('{} {}'.format(a + 1, b + 1))



N, M = map(int, input().split())
A = []
for i in range(N):
    row = [int(x) for x in input().split()]
    A.append(row)

solve(N, M, A)
