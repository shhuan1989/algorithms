# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/16/19

"""

import collections
import time
import os
import sys
import bisect
import heapq




def solve(N, A):
    A.sort()
    i = 0
    l, r = A[0][0], A[0][1]
    while i + 1 < N:
        if A[i + 1][0] <= r:
            r = max(r, A[i+1][1])
        else:
            ans = [0] * N
            for j in range(i+1):
                ans[A[j][2]] = 1
            for j in range(i+1, N):
                ans[A[j][2]] = 2
            
            return ' '.join(map(str, ans))
        
        i += 1
        
    return '-1'


T = int(input())
ans = []
for ti in range(T):
    N = int(input())
    segs = []
    for i in range(N):
        l, r = map(int, input().split())
        segs.append((l, r, i))
    
    ans.append(solve(N, segs))
    
print('\n'.join(ans))