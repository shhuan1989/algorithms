# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/10

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

def diff(a, b):
    return sum([1 if u != v else 0 for u, v in zip(a, b)])

def solve(N, M, A):
    def check(val):
        return all([diff(val, v) < 2 for v in A])
    
    ans = list(A[0])
    if check(ans):
        return ''.join(ans)
    
    for i, v in enumerate(ans):
        possible = {a[i] for a in A}
        for c in possible:
            ans[i] = c
            if check(ans):
                return ''.join(ans)
        ans[i] = v
            
    return '-1'
    

T = int(input())
ans = []
for ti in range(T):
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(input())
    ans.append(solve(N, M, A))

print('\n'.join(ans))
