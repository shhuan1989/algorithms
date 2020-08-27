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

INF = 10**3+7
MAXN = 10 ** 4 + 5
MAXM = 10 ** 5
to = [-1 for _ in range(MAXM)]
cap = [0 for _ in range(MAXM)]
head = [0 for _ in range(MAXN)]
nxt = [0 for _ in range(MAXM)]

level = [0 for _ in range(MAXN)]
pre = [0 for _ in range(MAXN)]
prex = [0 for _ in range(MAXN)]
vis = [False for _ in range(MAXN)]
tot = [1]

edges = []


def getlabel(ou, tu):
    start, end, earth, moon = 0, N + 3, 1, N + 2
    if ou == start:
        return 'S'
    elif ou >= end:
        return 'T'
    elif ou == earth:
        return 'E'
    elif ou == moon:
        return 'M'
    else:
        return '{}-{}'.format(ou-1, tu)


def draw():
    import networkx as nx
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('MacOSX')
    
    # plt.ion()
    plt.figure()
    g = nx.DiGraph()
    node_labels = {}
    edge_labels = {}
    pos = {}
    
    for u, v, w, ou, ov, tu, tv in edges:
        pos[u] = (ou, tu)
        pos[v] = (ov, t)
        g.add_edge(u, v)
        edge_labels[(u, v)] = w if w < INF else ''
        node_labels[u] = getlabel(ou, tu)
        node_labels[v] = getlabel(ov, tv)
        
    print(pos)
    # pos = nx.shell_layout(g)
    nx.draw(g, pos)
    nx.draw_networkx_labels(g, pos, node_labels)
    nx.draw_networkx_edge_labels(g, pos, edge_labels)
    plt.show()


def add_edge(u, v, w):
    tot[0] += 1
    t = tot[0]
    to[t] = v
    cap[t] = w
    nxt[t] = head[u]
    head[u] = t

def add(u, v, w, ou, ov, tu, tv):
    add_edge(u, v, w)
    add_edge(v, u, 0)
    
    edges.append((u, v, w, ou, ov, tu, tv))


def bfs(start, end):
    for i in range(MAXN):
        level[i] = -1
    
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
    i = head[curr]
    while i > 0 and add > 0:
        v = to[i]
        if level[v] == level[curr] + 1 and cap[i] > 0:
            f = dfs(v, end, min(add, cap[i]))
            if f > 0:
                add -= f
                flow += f
                cap[i] -= f
                cap[i ^ 1] += f
            
        i = nxt[i]
    
    return flow


def max_flow(start, end):
    ans = 0
    while bfs(start, end):
        ans += dfs(start, end, INF)
            
    return ans
    

parent = [i for i in range(55)]
def find(u):
    pu = parent[u]
    if pu == u:
        return u
    
    pu = find(pu)
    parent[u] = pu
    return pu


def merge(u, v):
    pu, pv = find(u), find(v)
    parent[pu] = pv
    
    
def check(S, start, end):
    for s in S:
        for v in s:
            merge(s[0], v)
    
    return find(start) == find(end)


if __name__ == '__main__':
    # sys.stdin = open('p2754_2.in', 'r')
    N, M, K = map(int, input().split())
    H = []
    S = []
    
    start, end, earth, moon = 0, N+3, 1, N + 2
    
    for i in range(M):
        row = [int(x) for x in input().split()]
        H.append(row[0])
        s = [v+1 if v > 0 else (earth if v == 0 else moon) for v in row[2:]]
        S.append(s)
    
    if not check(S, earth, moon):
        print(0)
        exit(0)
        
    
    def getpos(ship, t):
        return S[ship][t % len(S[ship])]

    def getid(pos, t):
        return t * 20 + pos + 1
    
    # add(start, getid(earth, 0), INF, start, earth, 0, 0)
    # add(getid(moon, 0), end, INF, moon, N+3, 0, 0)
    t = 0
    f = 0
    while True:
        if tot[0] >= MAXN:
            print(0)
            break
        
        add(start, getid(earth, t), INF, start, earth, 0, t)
        add(getid(moon, t), end, INF, moon, end, t, 0)
        # add(getid(earth, t-1), getid(earth, t), INF, earth, earth, t-1, t)
        # add(getid(moon, t-1), getid(moon, t-1), INF, moon, moon, t-1, t)
        if t > 0:
            for i in range(2, N+2):
                add(getid(i, t-1), getid(i, t), INF, i, i, t-1, t)
            
            for ship in range(M):
                u, v = getpos(ship, t-1), getpos(ship, t)
                add(getid(u, t-1), getid(v, t), H[ship], u, v, t-1, t)
            
        f += max_flow(start, end)
        # print(t, f)
        if f >= K:
            # draw()
            print(t)
            exit(0)

        t += 1