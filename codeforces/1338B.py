# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/30

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


# def dfs(G, node, parent, dist):
#     if not node:
#         return dist % 2 == 0
#
#     isleaf = True
#     for u in G[node]:
#         if u != parent:
#             isleaf = False
#             if not dfs(G, u, node, dist+1):
#                 return False
#
#     return dist % 2 == 0 if isleaf else True
    

if __name__ == '__main__':
    N = int(input())
    G = [[] for _ in range(N+1)]
    
    for i in range(N-1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    
    leafs = [i for i in range(1, N+1) if len(G[i]) == 1]
    leafNeibs = set()
    for u in leafs:
        for v in G[u]:
            leafNeibs.add(v)
    
    maxv = (N - 1) - len(leafs) + len(leafNeibs)
    minv = 1
    
    q = [leafs[0]]
    dist = [N+1 for _ in range(N+1)]
    d = 0
    dist[leafs[0]] = 0
    while q:
        nq = []
        d += 1
        for u in q:
            for v in G[u]:
                if dist[v] == N+1:
                    dist[v] = d
                    nq.append(v)
        q = nq
    
    if any([dist[v] % 2 != 0 for v in leafs]):
        minv = 3
            
    print('{} {}'.format(minv, maxv))
