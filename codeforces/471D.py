# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/11/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



def solve_prefix(N, W, A, B):
    # https://cp-algorithms.com/string/prefix-function.html
    if len(B) == 1:
        return N

    A = [A[i] - A[i + 1] for i in range(N - 1)]
    B = [B[i] - B[i + 1] for i in range(W - 1)]

    v = max(max(A), max(B)) + 1
    C = B + [v] + A
    M = len(C)
    
    pi = [0 for _ in range(M)]
    for i in range(1, M):
        j = pi[i-1]
        while j > 0 and C[i] != C[j]:
            j = pi[j-1]
        if C[i] == C[j]:
            j += 1
        pi[i] = j
    return pi.count(W-1)



def solve_zfunc(N, W, A, B):
    # https://cp-algorithms.com/string/z-function.html
    
    if len(B) == 1:
        return N
    
    A = [A[i]-A[i+1] for i in range(N-1)]
    B = [B[i]-B[i+1] for i in range(W-1)]
    
    v = max(max(A), max(B)) + 1
    C = B + [v] + A
    M = len(C)
    z = [0 for _ in range(M)]
    l, r = 0, 0
    # i starts from 1
    for i in range(1, M):
        if i <= r:
            z[i] = min(z[i-l], r-i+1)
        while i + z[i] < M and C[z[i]] == C[i+z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            r = i + z[i] - 1
            l = i
    # print(C)
    # print(z)
    return z.count(W-1)
    

N, W = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

# print(solve_zfunc(N, W, A, B))
print(solve_prefix(N, W, A, B))