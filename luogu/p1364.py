# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/21

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
    g = [[] for _ in range(N+1)]
    W = [0 for _ in range(N+1)]
    for u in range(1, N+1):
        w, l, r = map(int, input().split())
        W[u] = w
        for v in [l, r]:
            if v > 0:
                g[u].append(v)
                g[v].append(u)
    
    size = [0 for _ in range(N+1)]
    cost = [0 for _ in range(N+1)]
    def dfs(u, p, d):
        # print(u, d)
        s, t = W[u], W[u] * d
        for v in g[u]:
            if v != p:
                dfs(v, u, d+1)
                s += size[v]
                t += cost[v]
        size[u] = s
        cost[u] = t
    
    dfs(1, -1, 0)
    # print(size)
    # print(cost)
    
    def dfs2(u, p):
        for v in g[u]:
            if v == p:
                continue
            cost[v] = cost[u] + size[1] - size[v] - size[v]
            dfs2(v, u)
    
    dfs2(1, -1)
    # print(cost)
    print(min(cost[1:]))