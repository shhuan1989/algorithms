# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/10/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


N, M = map(int, input().split())

A = [int(x) for x in input().split()]

S = []
for i in range(M):
    x, y, w = map(int, input().split())
    S.append((w, x, y))


U = [i for i in range(N+1)]


def root(node):
    if node == U[node]:
        return node
    
    u = root(U[node])
    U[node] = u
    
    return u
    

def union(u, v):
    u, v = root(u), root(v)
    if u == v:
        return False
    
    U[v] = u
    return True
    

if N == 1:
    print(0)
else:
    minVal = min(A)
    startNode = A.index(minVal)
    edges = [(minVal+A[i], startNode+1, i+1) for i in range(N)] + S
    edges.sort()
    ans = sum([w if union(x, y) else 0 for w, x, y in edges])
    print(ans)