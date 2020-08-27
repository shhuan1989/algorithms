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
import math

INF = 10 ** 9 + 7
MAXN = 5000
MAXM = 10 ** 5

head = [-1 for _ in range(MAXN)]
pre = [-1 for _ in range(MAXN)]
dist = [-1 for _ in range(MAXN)]
inq = [-1 for _ in range(MAXN)]
incf = [-1 for _ in range(MAXN)]

cap = [0 for _ in range(MAXM)]
to = [0 for _ in range(MAXM)]
nxt = [0 for _ in range(MAXM)]
cost = [0 for _ in range(MAXM)]

tot = [1]


def draw(start, end):
    import networkx as nx
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('MacOSX')
    
    plt.figure('{}->{}'.format(start, end))
    g = nx.MultiDiGraph()
    
    for i in range(MAXN):
        inq[i] = False
    
    edge_labels = {}
    for u in range(start, end):
        i = head[u]
        while i > 0:
            v = to[i]
            if cap[i] > 0:
                g.add_edge(u, v)
                edge_labels[(u, v)] = '{}-{}'.format(cap[i] if cap[i] != INF else 'inf', cost[i])
            i = nxt[i]
    
    pos = nx.shell_layout(g)
    nx.draw_networkx_nodes(g, pos)
    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_edges(g, pos)
    nx.draw_networkx_edge_labels(g, pos, edge_labels)
    plt.show()


def add_edge(u, v, w, c):
    tot[0] += 1
    i = tot[0]
    
    cap[i] = w
    to[i] = v
    cost[i] = c
    nxt[i] = head[u]
    head[u] = i


def add(u, v, w, c):
    add_edge(u, v, w, c)
    add_edge(v, u, 0, -c)


def spfa(start, end):
    for i in range(MAXN):
        dist[i] = -INF
        inq[i] = False
        incf[i] = 0
        pre[i] = -1
    
    q = collections.deque([start])
    inq[start] = True
    dist[start] = 0
    incf[start] = INF
    while q:
        u = q.popleft()
        inq[u] = False
        i = head[u]
        while i > 0:
            v = to[i]
            if cap[i] > 0 and dist[v] < dist[u] + cost[i]:
                dist[v] = dist[u] + cost[i]
                incf[v] = min(cap[i], incf[u])
                pre[v] = i
                if not inq[v]:
                    inq[v] = True
                    q.append(v)
            i = nxt[i]
    
    return dist[end] > 0


def max_flow_ek(start, end, id2rc):
    ans = 0
    path = []
    while spfa(start, end):
        u = end
        p = []
        np = []
        while u != start:
            cap[pre[u]] -= incf[end]
            cap[pre[u] ^ 1] += incf[end]
            pu = to[pre[u] ^ 1]
            
            r, c = id2rc[u]
            pr, pc = id2rc[pu]
            if r == pr and c == pc + 1:
                p.append(1)
            elif r == pr + 1 and c == pc:
                p.append(0)
            
            if not np or np[-1] != id2rc[u]:
                np.append(id2rc[u])
            u = pu
        ans += dist[end] * incf[end]
        # print(np[::-1])
        path.append(p[::-1])
    
    return path


if __name__ == '__main__':
    # sys.stdin = open('p3356.in', 'r')
    K = int(input())
    M = int(input())
    N = int(input())
    
    A = []
    for i in range(N):
        row = [int(x) for x in input().split()]
        A.append(row)
    
    def getid(r, c, k):
        return r * M + c + 1 + k * N * M
    
    start, end = 0, getid(N-1, M-1, 1) + 1
    
    add(start, getid(0, 0, 0), K, 0)
    
    
    id2rc = {start: (0, 0), end: (N-1, M-1)}
    for r in range(N):
        for c in range(M):
            id2rc[getid(r, c, 0)] = (r, c)
            id2rc[getid(r, c, 1)] = (r, c)
            
    for r in range(N):
        for c in range(M):
            if A[r][c] == 1:
                continue

            add(getid(r, c, 0), getid(r, c, 1), INF, 0)
            if A[r][c] == 2:
                add(getid(r, c, 0), getid(r, c, 1), 1, 1)
                
            if c + 1 < M:
                if A[r][c + 1] != 1:
                    add(getid(r, c, 1), getid(r, c+1, 0), INF, 0)
            if r + 1 < N:
                if A[r+1][c] != 1:
                    add(getid(r, c, 1), getid(r+1, c, 0), INF, 0)
    
    add(getid(N-1, M-1, 1), end, INF, 0)
    # draw(start, end)
    # print(max_flow_ek(start, end, id2rc))
    ans = max_flow_ek(start, end, id2rc)
    for i, p in enumerate(ans):
        print('\n'.join(['{} {}'.format(i+1, v) for v in p]))
    
    
    