# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/8

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

def solve(N, A, B):
    
    if N % 2 != 0:
        if A[N//2] != B[N//2]:
            return False
    
    wca = collections.defaultdict(int)
    for i in range(N//2):
        a, b = A[i], A[N-i-1]
        wca[min(a, b), max(a, b)] += 1
    wcb = collections.defaultdict(int)
    for i in range(N//2):
        a, b = B[i], B[N - i - 1]
        wcb[min(a, b), max(a, b)] += 1
    
    return all([wca[k] == v for k, v in wcb.items()])
        
    
    

T = int(input())
ans = []
for ti in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    ans.append(solve(N, A, B))
    
print('\n'.join(['Yes' if v else 'No' for v in ans]))