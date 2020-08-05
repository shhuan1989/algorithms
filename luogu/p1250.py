# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/3

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
    H = int(input())
    
    link = [0 for _ in range(N+1)]
    to = [0 for _ in range(2*N+H+10)]
    nxt = [0 for _ in range(2*N+H+10)]
    W = [0 for _ in range(2*N+H+10)]
    tot = [0]
    
    def add(u, v, w):
        tot[0] += 1
        t = tot[0]
        to[t] = v
        nxt[t] = link[u]
        W[t] = w
        link[u] = t
    
    
    for i in range(H):
        s, t, c = map(int, input().split())
        # G[s].append((t-1, -c))
        add(s-1, t, c)

    dist = [0 for _ in range(N + 1)]
    for v in range(N+1):
        if v != 0:
            add(v-1, v, 0)
            dist[v] = float('-inf')
        if v != N:
            add(v, v-1, -1)
    
    q = collections.deque([0])
    inq = [False for _ in range(N+1)]
    
    while q:
        u = q.popleft()
        inq[u] = False
        i = link[u]
        while i > 0:
            if dist[to[i]] < dist[u] + W[i]:
                dist[to[i]] = dist[u] + W[i]
                if not inq[to[i]]:
                    q.append(to[i])
                    inq[to[i]] = True
            i = nxt[i]
    
    print(dist[N])
