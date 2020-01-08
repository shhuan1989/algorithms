# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/27/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

def getid(ch):
    return ord(ch) - ord('a')

def solve(N, A):
    
    g = [[False for _ in range(26)] for _ in range(26)]
    for i in range(N-1):
        pos, a, b = 0, A[i], A[i+1]
        while pos < min(len(a), len(b)) and a[pos] == b[pos]:
            pos += 1
        if len(b) <= pos < len(a):
            return 'Impossible'
        if pos < min(len(a), len(b)):
            g[getid(a[pos])][getid(b[pos])] = True
        
    for k in range(26):
        for i in range(26):
            for j in range(26):
                g[i][j] = g[i][j] or (g[i][k] and g[k][j])
    
    # cycle
    if any([g[i][i] for i in range(26)]):
        return 'Impossible'
    
    vis = [False for _ in range(26)]
    ans = ''
    for i in range(26):
        for j in range(26):
            valid = not vis[j]
            for k in range(26):
                if not vis[k] and g[k][j]:
                    valid = False
                    break
            if valid:
                vis[j] = True
                ans += chr(ord('a') + j)
                break
    return ans
    
            
        

N = int(input())
A = []
for i in range(N):
    A.append(input())
# N = 100
# A = []
# import  random
# for i in range(N):
#     A.append('a' * 100)
print(solve(N, A))