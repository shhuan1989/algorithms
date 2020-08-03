# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/14

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    MAXN = 100005
    N, M = map(int, input().split())
    C = [0] + [int(x) for x in input().split()]
    G = collections.defaultdict(list)
    RG = collections.defaultdict(list)
    for i in range(M):
        x, y, z = map(int, input().split())
        if z == 1:
            G[x].append(y)
            RG[y].append(x)
        else:
            G[x].append(y)
            G[y].append(x)
            RG[x].append(y)
            RG[y].append(x)
    
    
    def spfa(start, graph, findmax):
        q = collections.deque([start])
        inq = [False for _ in range(N + 1)]
        res = [0 if findmax else 10 ** 7 for _ in range(N + 1)]
        res[start] = C[start]
        inq[start] = True
        while q:
            u = q.popleft()
            inq[u] = False
            s = res[u]
            for v in graph[u]:
                ns = max(C[v], s) if findmax else min(C[v], s)
                if ns > res[v] if findmax else ns < res[v]:
                    res[v] = ns
                    if not inq[v]:
                        q.append(v)
                        inq[v] = True
        return res
    
    a, b = spfa(1, G, False), spfa(N, RG, True)
    # print(a)
    # print(b)
    ans = max([b[v]-a[v] for v in range(1, N+1)])
    print(ans)
