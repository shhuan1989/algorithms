# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/8/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, A):
    A = [float('inf')] + A + [float('inf')]
    left = [0 for i in range(N+2)]
    right = [N+1 for i in range(N+2)]
    
    q = []
    for i, v in enumerate(A):
        while q and q[-1][1] > v:
            j, u = q.pop()
            right[j] = i
        
        if q:
            j, u = q[-1]
            left[i] = j
        q.append((i, v))
    
    # print(left)
    # print(right)
    
    ans = [0 for _ in range(N+1)]
    # for i, v in enumerate(A):
    #     for l in range(right[i]-left[i]):
    #         ans[l] = max(ans[l], v)
    
    p = [0 for _ in range(N+2)]
    for i, v in enumerate(A):
        l = right[i] - left[i] - 1
        p[l] = max(p[l], v)
    
    maxv = 0
    for i in range(N, -1, -1):
        maxv = max(p[i], maxv)
        ans[i] = maxv
        
    print(' '.join(map(str, ans[1:])))
    
    
    
    
N = int(input())
A = [int(x) for x in input().split()]
solve(N, A)