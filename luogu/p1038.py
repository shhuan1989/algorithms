# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/9

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



if __name__ == '__main__':
    N, P = map(int, input().split())
    
    C = [0 for _ in range(N+1)]
    U = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        c, u = map(int, input().split())
        C[i] = c
        U[i] = u
    W = [[0 for _ in range(N+1)] for _ in range(N+1)]
    G = collections.defaultdict(list)
    for i in range(P):
        u, v, w = map(int, input().split())
        G[u].append(v)
        W[u][v] = w
    
    # print(C)
    # print(U)
    q = [i for i in range(1, N+1) if C[i] - U[i] > 0]
    while q:
        # print(q)
        # print(C)
        for u in q:
            for v in G[u]:
                C[v] += (C[u]-U[u]) * W[u][v]

            C[u] = U[u]
        q = [i for i in range(1, N+1) if C[i] - U[i] > 0]
    
    # print(C)
    for i in range(1, N+1):
        if C[i] != 0:
            print('{} {}'.format(i, C[i]))
        
    