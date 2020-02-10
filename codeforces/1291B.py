# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/3/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



def solve(N, A):
    if all([v >= i for i, v in enumerate(A)]):
        return True
    
    B = A[::-1]
    if all([v >= i for i, v in enumerate(B)]):
        return True
    
    i = min([i for i, v in enumerate(A) if v < i])
    v = min(A[i], A[i-1]-1)
    
    if v < 0:
        return False
    
    for j in range(i+1, N):
        v = min(v-1, A[j])
        if v < 0:
            return False
        
    return True


T = int(input())
ans = []
for ti in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    ans.append(solve(N, A))

print('\n'.join(['YES' if x else 'NO' for x in ans]))
