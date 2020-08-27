# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/5

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

MAXN = 2000
MAXM = 10005
INF = 10 ** 9 + 7

head = [-1 for _ in range(MAXN)]
vis = [False for _ in range(MAXN)]
pre = [-1 for _ in range(MAXN)]
incf = [0 for _ in range(MAXN)]
dist = [0 for _ in range(MAXN)]

cap = [0 for _ in range(MAXM)]
nxt = [-1 for _ in range(MAXM)]
cost = [-1 for _ in range(MAXM)]
to = [-1 for _ in range(MAXM)]

tot = [1]


def add_edge(u, v, w, c):
    tot[0] += 1
    i = tot[0]
    cap[i] = w
    cost[i] = c
    to[i] = v
    nxt[i] = head[u]
    head[u] = i


def add(u, v, w, c):
    add_edge(u, v, w, c)
    add_edge(v, u, 0, -c)


def spfa(start, end, maxfee):
    for i in range(MAXN):
        pre[i] = -1
        dist[i] = -INF if maxfee else INF
        vis[i] = False
    
    vis[start] = True
    dist[start] = 0
    incf[start] = INF
    q = collections.deque([start])
    while q:
        u = q.popleft()
        i = head[u]
        vis[u] = False
        while i > 0:
            v = to[i]
            f = min(cap[i], incf[u])
            if f <= 0:
                i = nxt[i]
                continue
            
            nd = dist[u] + cost[i]
            if (dist[v] < nd) if maxfee else (dist[v] > nd):
                dist[v] = nd
                pre[v] = i
                incf[v] = f
                if not vis[v]:
                    vis[v] = True
                    q.append(v)
            
            i = nxt[i]
    
    return dist[end] > -INF if maxfee else dist[end] < INF


def max_flow(start, end, maxfee):
    ans, flow = 0, 0
    while spfa(start, end, maxfee):
        u = end
        flow += incf[end]
        # path = []
        while u != start:
            # path.append(u)
            ans += incf[end] * cost[pre[u]]
            cap[pre[u]] -= incf[end]
            cap[pre[u] ^ 1] += incf[end]
            u = to[pre[u] ^ 1]
        # print(path[::-1], ans)
    return ans


if __name__ == '__main__':
    # sys.stdin = open('p4012.in', 'r')
    a, b = map(int, input().split())
    p, q = map(int, input().split())
    
    sn = []
    for i in range(p + 1):
        row = [int(x) for x in input().split()]
        sn.append(row)
    
    we = []
    for i in range(q + 1):
        row = [int(x) for x in input().split()]
        we.append(row)
    
    
    def getid(r, c):
        return r * 20 + c + 10
    
    
    # vmap = {}
    # for r in range(q+1):
    #     for c in range(p+1):
    #         vmap[getid(r, c)] = (r, c)
    #
    # print(vmap)
    
    start, end = 0, getid(p, q) + 10
    for i in range(a):
        k, x, y = map(int, input().split())
        add(start, getid(x, y), k, 0)
    
    for r in range(p + 1):
        for c in range(q):
            add(getid(r, c), getid(r, c + 1), 1, sn[r][c])
            add(getid(r, c), getid(r, c + 1), INF, 0)
    
    for c in range(q + 1):
        for r in range(p):
            add(getid(r, c), getid(r + 1, c), 1, we[c][r])
            add(getid(r, c), getid(r + 1, c), INF, 0)
    
    for i in range(b):
        r, x, y = map(int, input().split())
        add(getid(x, y), end, r, 0)
    
    print(max_flow(start, end, True))
