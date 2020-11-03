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

MAXN = 500
MAXM = 10000
INF = 10 ** 9 + 7
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


def desc():
    
    for u in range(MAXN):
        i = head[u]
        while i > 0:
            v = to[i]
            if cap[i] > 0:
                print(u, v, cap[i])
            i = nxt[i]



if __name__ == '__main__':
    # sys.stdin = open('P1345_1.in', 'r')
    N, M, start, end = map(int, input().split())
    
    
    def getid(x, t):
        return x + t * N
    
    # start, end = 0, getid(N+1, 1)
    # add(start, getid(c1, 0), INF)
    # add(getid(c2, 1), end, INF)
    
    for i in range(1, N+1):
        add(getid(i, 0), getid(i, 1), 1)
        
    
    for _ in range(M):
        u, v = map(int, input().split())
        add(getid(u, 1), getid(v, 0), INF)
        add(getid(v, 1), getid(u, 0), INF)
    
    # desc()
    ans = dinic(getid(start, 1), getid(end, 0))
    print(ans)
