# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/6

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

INF = 10**9+7

MAXN = 10005
MAXM = 10**5

head = [-1 for _ in range(MAXN)]
level = [-1 for _ in range (MAXN)]
vis = [False for _ in range(MAXN)]
curindex = [-1 for _ in range(MAXN)]
pre = [-1 for _ in range (MAXN)]
dist = [-1 for _ in range (MAXN)]
incf = [-1 for _ in range(MAXN)]

cap = [-1 for _ in range(MAXM)]
to = [-1 for _ in range(MAXM)]
nxt = [-1 for _ in range(MAXM)]
tot = [1]


def add_edge(u, v, w):
    tot[0] += 1
    i = tot[0]
    cap[i] = w
    to[i] = v
    nxt[i] = head[u]
    head[u] = i


def add(u, v, w):
    add_edge(u, v, w)
    add_edge(v, u, 0)


def bfs(start, end):
    for i in range(MAXN):
        level[i] = -1
        curindex[i] = head[i]
        
    level[start] = 0
    q = collections.deque([start])
    while q:
        u = q.popleft()
        i = head[u]
        while i > 0:
            v = to[i]
            if level[v] < 0 and cap[i] > 0:
                level[v] = level[u] + 1
                q.append(v)
            i = nxt[i]
            
    return level[end] > 0


def dfs(curr, end, add):
    if curr == end or add <= 0:
        return add
    
    flow = 0
    i = curindex[curr]
    while i > 0 and add > 0:
        curindex[curr] = i
        v = to[i]
        if level[v] == level[curr] + 1 and cap[i] > 0:
            f = dfs(v, end, min(cap[i], add))
            if f > 0:
                flow += f
                add -= f
                cap[i] -= f
                cap[i ^ 1] += f
        i = nxt[i]
    
    return flow


def spfa(start, end):
    for i in range(MAXN):
        vis[i] = False
        pre[i] = -1
        dist[i] = INF
        incf[i] = 0
        
    dist[start] = 0
    q = collections.deque([start])
    vis[start] = True
    incf[start] = INF
    while q:
        u = q.popleft()
        i = head[u]
        while i > 0:
            v = to[i]
            # f = min(cap[i], incf[u])
            if cap[i] > 0 and dist[v] > dist[u] + 1:
                dist[v] = dist[u] + 1
                pre[v] = i
                incf[v] = min(cap[i], incf[u])
                if not vis[v]:
                    q.append(v)
                    vis[v] = True
            i = nxt[i]
            
    return dist[end] < INF
    

def max_flow(start, end):
    ans = 0
    # while bfs(start, end):
    #     ans += dfs(start, end, INF)
    while spfa(start, end):
        ans += incf[end]
        u = end
        while u != start:
            cap[pre[u]] -= incf[end]
            cap[pre[u] ^ 1] += incf[end]
            u = to[pre[u] ^ 1]
    return ans


def getid(r, c, m):
    return (r-1)*m+c


if __name__ == '__main__':
    # sys.stdin = open('P2774_3.in', 'r')
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        row = [int(x) for x in input().split()]
        A.append(row)
    
    start, end = 0, M*N+1
    a = []
    b = []
    for r in range(1, N+1):
        for c in range(1, M+1):
            if (r+c) % 2 == 0:
                a.append((getid(r, c, M), A[r-1][c-1]))
            else:
                b.append((getid(r, c, M), A[r-1][c-1]))
    
    for i, v in a:
        add(start, i, v)
    
    for r in range(1, N+1):
        for c in range(1, M+1):
            if (r + c) % 2 == 0:
                u = getid(r, c, M)
                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 1 <= nr <= N and 1 <= nc <= M:
                        v = getid(nr, nc, M)
                        add(u, v, INF)
    
    for i, v in b:
        add(i, end, v)
    
    s = sum([sum(row) for row in A])
    
    print(s - max_flow(start, end))
            
    