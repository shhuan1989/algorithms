# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/15

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

MAXN = 50
MAXM = 10000
INF = 10**15 + 7
head = [-1 for _ in range(MAXN)]
depth = [-1 for _ in range(MAXN)]

cap = [0 for _ in range(MAXM)]
flow = [0 for _ in range(MAXM)]
to = [-1 for _ in range(MAXM)]
nxt = [-1 for _ in range(MAXM)]

tot = [1]

def add_edge(u, v, w):
    tot[0] += 1
    i = tot[0]
    to[i] = v
    cap[i] = w
    flow[i] = 0
    nxt[i] = head[u]
    head[u] = i


def add(u, v, w):
    add_edge(u, v, w)
    add_edge(v, u, 0)


def bfs(start, end):
    for i in range(MAXN):
        depth[i] = -1
    
    depth[start] = 0
    q = collections.deque([start])
    
    while q:
        u = q.popleft()
        i = head[u]
        while i > 0:
            v = to[i]
            if depth[v] < 0 and cap[i] - flow[i] > 0:
                depth[v] = depth[u] + 1
                q.append(v)
            i = nxt[i]
    
    return depth[end] > 0


def dfs(curr, end, add):
    if curr == end or add <= 0:
        return add
    
    maxflow = 0
    i = head[curr]
    while i > 0 and add > 0:
        v = to[i]
        if depth[v] == depth[curr] + 1 and cap[i] - flow[i] > 0:
            f = dfs(v, end, min(add, cap[i] - flow[i]))
            if f > 0:
                add -= f
                maxflow += f
                flow[i] += f
                flow[i ^ 1] -= f
        i = nxt[i]
        
    return maxflow


def dinic(start, end):
    ans = 0
    while bfs(start, end):
        ans += dfs(start, end, INF)
    
    return ans

if __name__ == '__main__':
    N, M = map(int, input().split())
    
    start, end = 0, N+1
    add(start, 1, INF)
    add(N, end, INF)
    a = 10000
    for _ in range(M):
        u, v, c = map(int, input().split())
        add(u, v, c*a+1)
    
    ans = dinic(start, end)
    print(ans//a, ans%a)
    