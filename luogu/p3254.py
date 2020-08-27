# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/7

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

MAXN = 2000
MAXM = 500000
INF = 10**9 + 7

head = [-1 for _ in range(MAXN)]
level = [-1 for _ in range(MAXN)]
vis = [False for _ in range(MAXN)]

cap = [-1 for _ in range(MAXM)]
nxt = [-1 for _ in range(MAXM)]
to = [-1 for _ in range(MAXM)]

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
        vis[i] = False
        level[i] = -1
        
    level[start] = 0
    q = collections.deque([start])
    while q:
        u = q.popleft()
        i = head[u]
        while i > 0:
            v = to[i]
            if cap[i] > 0 and level[v] < 0:
                level[v] = level[u] + 1
                q.append(v)
            i = nxt[i]
    
    return level[end] > 0


def dfs(curr, end, add):
    if curr == end or add <= 0:
        return add
    
    flow = 0
    i = head[curr]
    while i > 0 and add > 0:
        v = to[i]
        if cap[i] > 0 and level[v] == level[curr] + 1:
            f = dfs(v, end, min(add, cap[i]))
            if f > 0:
                flow += f
                add -= f
                cap[i] -= f
                cap[i ^ 1] += f
        i = nxt[i]
        
    return flow

def dinic(start, end):
    ans = 0
    while bfs(start, end):
        ans += dfs(start, end, INF)
    return ans


if __name__ == '__main__':
    # sys.stdin = open('p3254_11.in', 'r')
    N, M = map(int, input().split())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    
    start, end = 0, M+N+1
    
    for u in range(1, N+1):
        add(start, u, A[u-1])
    
    for u in range(1, N+1):
        for v in range(1, M+1):
            add(u, N+v, 1)
    
    for u in range(1, M+1):
        add(N+u, end, B[u-1])
        
    flow = dinic(start, end)
    if flow < sum(A):
        print(0)
    else:
        print(1)
        
        for u in range(1, N+1):
            i = head[u]
            table = []
            while i > 0:
                v = to[i]
                if N+1 <= v <= N+M and cap[i] == 0:
                    table.append(v-N)
                i = nxt[i]
            print(' '.join(map(str, table)))
