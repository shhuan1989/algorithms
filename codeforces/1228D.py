# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/16/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, M, g):
    if M < N - 1:
        print(-1)
        return
    
    mark = [1 for _ in range(N+1)]
    mark[1] = 1
    mark[0] = 0
    
    b = 0
    for v in g[1]:
        mark[v] = 2
        b = v

    for v in g[b]:
        if mark[v] == 2:
            mark[v] = 3
            
    na, nb, nc = mark.count(1), mark.count(2), mark.count(3)
    if M != na * nb + nb * nc + na * nc or any([n == 0 for n in [na, nb, nc]]):
        print(-1)
        return
    
    ns = [0, na, nb, nc]
    
    for u in range(1, N+1):
        v = g[u]
        if len(v) != N - ns[mark[u]]:
            print(-1)
            return
        wc = collections.Counter([mark[x] for x in v])
        for k, c in wc.items():
            if c != ns[k]:
                print(-1)
                return
            
    print(' '.join(map(str, mark[1:])))

    
N, M = map(int, input().split())
g = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
    
solve(N, M, g)