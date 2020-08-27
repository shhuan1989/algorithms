# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/14

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

INF = 10**9 + 7

MAXN = 5000
MAXM = 10**5

head = [-1 for _ in range(MAXN)]
dep = [-1 for _ in range(MAXN)]

to = [-1 for _ in range(MAXM)]
nxt = [-1 for _ in range(MAXM)]
cap = [-1 for _ in range(MAXM)]
flow = [-1 for _ in range(MAXM)]

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


def reset():
    tot[0] = 1
    for i in range(MAXN):
        head[i] = -1
        dep[i] = -1
        
    for i in range(MAXM):
        to[i] = -1
        flow[i] = 0
        cap[i] = -1
        nxt[i] = -1


def bfs(start, end):
    for i in range(MAXN):
        dep[i] = -1
        
    dep[start] = 0
    q = collections.deque([start])
    while q:
        u = q.popleft()
        i = head[u]
        while i > 0:
            v = to[i]
            if dep[v] < 0 and cap[i] - flow[i] > 0:
                dep[v] = dep[u] + 1
                q.append(v)
            i = nxt[i]
    
    return dep[end] > 0


def dfs(u, end, add):
    if u == end or add <= 0:
        return add
    
    fl = 0
    i = head[u]
    while i > 0 and add > 0:
        v = to[i]
        if dep[v] == dep[u] + 1 and cap[i] - flow[i] > 0:
            f = dfs(v, end, min(add, cap[i] - flow[i]))
            if f > 0:
                add -= f
                fl += f
                flow[i] += f
                flow[i ^ 1] -= f
            
        i = nxt[i]
        
    return fl


def max_flow(start, end):
    f = 0
    while bfs(start, end):
        f += dfs(start, end, INF)
    
    return f


def getnode(x):
    if x == 0:
        return 'S'
    
    if x <= N:
        return x
    
    if x < 3 * N * N:
        x %= N * N
        x -= 1
        a = x // N
        b = x % N
        return '{}-{}'.format(a + 1, b + 1)
    
    return 'T'

def draw():
    print('=' * 80)
    for u in range(MAXN):
        i = head[u]
        while i > 0:
            if cap[i] > 0:
                print('{} {} {}'.format(getnode(u), getnode(to[i]), cap[i]))
            i = nxt[i]


if __name__ == '__main__':
    # sys.stdin = open('p1264.in', 'r')
    N = int(input())
    A = [int(x) for x in input().split()]
    win = A[::2]
    A = [int(x) for x in input().split()]
    
    game = [[0 for _ in range(N)] for _ in range(N)]
    
    for i, v in enumerate(A):
        r, c = i // N, i % N
        game[r][c] = v
    
    def getid(r, c, k):
        return r*N+c+1 + k*N*N
    
    ans = []
    for team in range(N):
        # build graph
        maxscore = win[team]
        for v in range(N):
            maxscore += game[team][v]
        if maxscore < max(win):
            continue
            
        start, end = 0, getid(N, N, 2) + 1
        reset()
        rest = 0
        for u in range(N):
            for v in range(u + 1, N):
                if u == team or v == team:
                    continue
                
                rest += game[u][v]
                mid = getid(u, v, 1)
                add(start, mid, game[u][v])
                add(mid, u + 1, INF)
                add(mid, v + 1, INF)
            add(u + 1, end, maxscore-win[u])
        # draw()
        f = max_flow(start, end)
        if f >= rest:
            ans.append(team + 1)
    
    print(' '.join(map(str, ans)))
    
    
    
    
    