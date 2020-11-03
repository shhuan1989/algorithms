# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/27

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



if __name__ == '__main__':
    N = int(input())
    line = input().strip()
    
    A = [0 if v == 'N' else (1 if v == 'O' else 2) for v in line]
    def solve(s):
        n = len(s)
        a, b, c = 0, 0, 0
        
        for i, v in enumerate(s):
            na, nb, nc = a, b, c
            
            if v == 0:
                na += 1
            elif v == 1:
                nb += a
            else:
                nc += b
            
            a, b, c = na, nb, nc
        
        return c

    
    ans = max(solve([0] + A), solve(A + [2]))
    
    
    left = [0 for _ in range(N+1)]
    for i, v in enumerate(A):
        left[i+1] = left[i]
        if v == 0:
            left[i+1] += 1
    
    right = [0 for _ in range(N+1)]
    for i in range(N-1, -1, -1):
        right[i] = right[i+1]
        if A[i] == 2:
            right[i] += 1
    
    o = 0
    for i in range(1, N):
        o = max(o, left[i] * right[i])
    
    # print(left)
    # print(right)
    # print(o)
    
    ans = max(ans, o)
        
    
    
    print(ans)