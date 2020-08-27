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
inq = [False for _ in range(MAXN)]
incf = [0 for _ in range(MAXN)]

cap = [0 for _ in range(MAXM)]
to = [-1 for _ in range(MAXM)]
nxt = [-1 for _ in range(MAXM)]
cost = [0 for _ in range(MAXM)]

tot = [1]

def reset():
    tot[0] = 1
    for i in range(MAXN):
        head[i] = -1
        pre[i] = -1
        dist[i] = -1
        inq[i] = False
        incf[i] = 0
    
    for i in range(MAXM):
        cap[i] = 0
        to[i] = -1
        nxt[i] = -1
        cost[i] = 0
        
    

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


def max_flow_ek(start, end):
    ans = 0
    while spfa(start, end):
        u = end
        while u != start:
            cap[pre[u]] -= incf[end]
            cap[pre[u] ^ 1] += incf[end]
            u = to[pre[u] ^ 1]
        ans += dist[end] * incf[end]
    
    return ans


if __name__ == '__main__':
    # sys.stdin = open('p4013.in', 'r')
    M, N = map(int, input().split())
    
    A = []
    C = [0]
    for i in range(N):
        row = [int(x) for x in input().split()]
        A.append(row)
        C.append(C[-1] + len(row))
    
    def get_id(r, c, t):
        return C[r] + c + 1 + C[-1]*t
    
    start, end = 0, 2 * C[-1] + 1000
    
    # q1
    for c in range(M):
        add(start, get_id(0, c, 0), 1,  0)
    
    for r in range(N-1):
        row = A[r]
        for c in range(len(row)):
            add(get_id(r, c, 0), get_id(r, c, 1), 1, A[r][c])
            add(get_id(r, c, 1), get_id(r+1, c, 0), 1, 0)
            add(get_id(r, c, 1), get_id(r+1, c+1, 0), 1, 0)
    
    for c in range(len(A[-1])):
        add(get_id(N-1, c, 0), get_id(N-1, c, 1), 1, A[N-1][c])
        add(get_id(N-1, c, 1), end, 1, 0)
    
    print(max_flow_ek(start, end))
    
    
    # q2
    reset()
    for c in range(M):
        add(start, get_id(0, c, 0), 1, 0)

    for r in range(N - 1):
        row = A[r]
        for c in range(len(row)):
            add(get_id(r, c, 0), get_id(r, c, 1), INF, A[r][c])
            add(get_id(r, c, 1), get_id(r + 1, c, 0), 1, 0)
            add(get_id(r, c, 1), get_id(r + 1, c + 1, 0), 1, 0)

    for c in range(len(A[-1])):
        add(get_id(N - 1, c, 0), get_id(N - 1, c, 1), INF, A[N - 1][c])
        add(get_id(N - 1, c, 1), end, INF, 0)

    print(max_flow_ek(start, end))

    # q3
    reset()
    for c in range(M):
        add(start, get_id(0, c, 0), 1, 0)

    for r in range(N - 1):
        row = A[r]
        for c in range(len(row)):
            add(get_id(r, c, 0), get_id(r, c, 1), INF, A[r][c])
            add(get_id(r, c, 1), get_id(r + 1, c, 0), INF, 0)
            add(get_id(r, c, 1), get_id(r + 1, c + 1, 0), INF, 0)

    for c in range(len(A[-1])):
        add(get_id(N - 1, c, 0), get_id(N - 1, c, 1), INF, A[N - 1][c])
        add(get_id(N - 1, c, 1), end, INF, 0)

    print(max_flow_ek(start, end))
    

    
    