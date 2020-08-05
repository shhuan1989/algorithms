# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/3

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

MAXN = 10**3
MAXM = 10**5
to = [-1 for _ in range(MAXM)]
cap = [0 for _ in range(MAXM)]
link = [0 for _ in range(MAXN)]
nxt = [0 for _ in range(MAXM)]
flow = [0 for _ in range(MAXN)]
pre = [0 for _ in range(MAXN)]
prex = [0 for _ in range(MAXN)]
vis = [False for _ in range(MAXN)]

tot = [1]

def add(u, v, w):
    tot[0] += 1
    t = tot[0]
    to[t] = v
    cap[t] = w
    nxt[t] = link[u]
    link[u] = t


def bfs(start, end):
    for i in range(MAXN):
        pre[i] = -1
        prex[i] = -1
        flow[i] = 0
        vis[i] = False
    
    flow[start] = 10**7
    q = collections.deque([start])
    vis[start] = True
    while q:
        u = q.popleft()
        i = link[u]
        while i > 0:
            v = to[i]
            if cap[i] > 0 and not vis[v]:
                vis[v] = True
                flow[v] += min(cap[i], flow[u])
                pre[v] = i
                prex[v] = u
                q.append(v)
            i = nxt[i]
        if flow[end] > 0:
            return True
            
    return False
    
    
def max_flow(start, end):
    ans = 0
    math = []
    while bfs(start, end):
        ans += flow[end]
        
        u = prex[end]
        v = prex[u]
        u, v = min(u, v), max(u, v)
        math.append((u, v))
        
        u = end
        while u >= 0:
            cap[pre[u]] -= flow[end]
            cap[pre[u] ^ 1] += flow[end]
            u = prex[u]
            
    print(ans)
    math.sort()
    print('\n'.join(['{} {}'.format(u, v) for u, v in math]))



if __name__ == '__main__':
    sys.stdin = open('P2756_6.in', 'r')
    M, N = map(int, input().strip().split())
    while True:
        u, v = map(int, input().strip().split())
        if u == -1 and v == -1:
            break
        if 1 <= u <= M and 1 <= v <= N:
            add(u, v, 1)
            add(v, u, 0)
    
    start, end = 0, N + 1
    for i in range(1, M+1):
        add(start, i, 1)
        add(i, start, 0)
    
    for i in range(M+1, N+1):
        add(i, end, 1)
        add(end, i, 0)
    
    max_flow(start, end)
    