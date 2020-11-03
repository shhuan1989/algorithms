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

INF = 10**9+7

MAXN = 5000
MAXM = 10**6 * 2

head = [-1 for _ in range(MAXN)]
depth = [-1 for _ in range(MAXN)]


cap = [-1 for _ in range(MAXM)]
flow = [0 for _ in range(MAXM)]
to = [-1 for _ in range(MAXM)]
nxt = [-1 for _ in range(MAXM)]

tot = [1]


def add_edge(u, v, w):
    tot[0] += 1
    i = tot[0]
    to[i] = v
    cap[i] = w
    nxt[i] = head[u]
    head[u] = i


def add(u, v, w):
    add_edge(u, v, w)
    add_edge(v, u, 0)


def bfs(start, end):
    for i in range(MAXN):
        depth[i] = -1
    
    q = collections.deque([start])
    depth[start] = 0
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
            f = dfs(v, end, min(cap[i] - flow[i], add))
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
    # sys.stdin = open('P1361_3.in', 'r')
    N = int(input())
    
    start, end = 0, MAXN-1
    
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    
    for u in range(1, N+1):
        add(start, u, A[u-1])
        add(u, end, B[u-1])
    
    M = int(input())
    groupid = N+1
    ans = sum(A) + sum(B)
    for _ in range(M):
        row = [int(x) for x in input().split()]
        pa, pb = row[1], row[2]
        seeds = row[2:]
        ans += pa + pb
        groupid += 1
        a, b = groupid, groupid+1
        groupid += 1
        add(start, a, pa)
        add(b, end, pb)
        for u in seeds:
            add(a, u, INF)
            add(u, b, INF)
    
    f = dinic(start, end)
    # print(ans, f)
    ans -= f
    print(ans)
    
    
        
