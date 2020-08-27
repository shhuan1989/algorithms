# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/21

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
    A = []
    for i in range(N):
        s = input().strip()
        A.append(s)
    G = collections.defaultdict(list)
    W = collections.defaultdict(int)
    for u in range(N):
        for v in range(N):
            if A[u][-1] == A[v][0]:
                G[u].append(v)
                W[u,v] = len(A[v])
    
    for i in range(N):
        G[N].append(i)
        W[N, i] = len(A[i])

    start = N
    q = collections.deque([(N, 0)])
    # inq = collections.defaultdict(bool)
    dist = collections.defaultdict(int)
    while q:
        u, s = q.popleft()
        # inq[u, s] = False
        
        for v in G[u]:
            if s & (1 << v):
                continue
            w = W[u, v]
            ns = s | (1 << v)
            if dist[v, ns] < dist[u, s] + w:
                dist[v, ns] = dist[u, s] + w
                # if not inq[v, ns]:
                #     inq[v, ns] = True
                q.append((v, ns))
    
    # print(len(dist))
    print(max(dist.values()))