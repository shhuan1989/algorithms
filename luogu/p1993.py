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
    N, M = map(int, input().split())
    
    link = [0 for _ in range(N+1)]
    to = [0 for _ in range(2*M + N + 10)]
    nxt = [0 for _ in range(2*M + N + 10)]
    weight = [0 for _ in range(2*M + N + 10)]
    tot = [0]
    
    def add(u, v, w):
        tot[0] += 1
        t = tot[0]
        nxt[t] = link[u]
        to[t] = v
        weight[t] = w
        link[u] = t
    
    for i in range(M):
        line = [int(x) for x in input().strip().split()]
        t = line[0]
        if t == 1:
            a, b, c = line[1:]
            add(a, b, -c)
        elif t == 2:
            a, b, c = line[1:]
            add(b, a, c)
        else:
            a, b = line[1:]
            add(a, b, 0)
            add(b, a, 0)
            
    for i in range(1, N+1):
        add(0, i, 0)
        
    dist = [float('inf') for _ in range(N+1)]
    inq = [False for _ in range(N+1)]
    count = [0 for _ in range(N+1)]
    q = collections.deque([0])
    dist[0] = 0
    while q:
        u = q.popleft()
        inq[u] = False
        i = link[u]
        while i > 0:
            v = to[i]
            if dist[v] > dist[u] + weight[i]:
                dist[v] = dist[u] + weight[i]
                if not inq[v]:
                    q.append(v)
                    inq[v] = True
                    count[v] += 1

                    if count[v] > N:
                        print('No')
                        exit(0)
            i = nxt[i]
    
    # print(dist)
    print('Yes')