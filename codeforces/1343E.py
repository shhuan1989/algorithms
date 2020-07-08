# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


INF = 2*10**5 + 10


def bfs(start, N, G):
    dist = [INF for _ in range(N + 1)]
    q = [start]
    dist[start] = 0
    while q:
        nq = []
        for u in q:
            d = dist[u] + 1
            for v in G[u]:
                if dist[v] > d:
                    dist[v] = d
                    nq.append(v)
        q = nq
        
    return dist
    
    

def solve(N, M, A, B, C, G, P):
    # path from A to B
    dista = bfs(A, N, G)
    distb = bfs(B, N, G)
    distc = bfs(C, N, G)

    P.sort()
    presum = [0]
    for v in P:
        presum.append(presum[-1] + v)

    ans = INF
    for mid in range(1, N+1):
        da, db, dc = dista[mid], distb[mid], distc[mid]
        dover = db
        dsingle = da + dc
        if dover + dsingle > M:
            continue
        ans = min(ans, presum[dover + dsingle] + presum[dover])
    
    return ans


if __name__ == '__main__':
    T = int(input())
    ans = []
    for ti in range(T):
        N, M, A, B, C = map(int, input().split())
        P = [int(x) for x in input().split()]
        G = collections.defaultdict(list)
        for i in range(M):
            u, v = map(int, input().split())
            G[u].append(v)
            G[v].append(u)
        
        ans.append(solve(N, M, A, B, C, G, P))
    
    print('\n'.join(map(str, ans)))
        


