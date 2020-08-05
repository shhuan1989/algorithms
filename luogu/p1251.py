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

MAXN = 5005
MAXM = 10**5
INF = 10**9+7

link = [0 for _ in range(MAXN)]
dist = [0 for _ in range(MAXN)]
flow = [0 for _ in range(MAXN)]
nxt = [-1 for _ in range(MAXM)]
to = [0 for _ in range(MAXM)]
cap = [0 for _ in range(MAXM)]
fee = [0 for _ in range(MAXM)]
pre = [0 for _ in range(MAXM)]
inq = [False for _ in range(MAXN)]
prex = [0 for _ in range(MAXN)]
tot = [1]


def add(u, v, w, f):
    tot[0] += 1
    t = tot[0]
    to[t] = v
    nxt[t] = link[u]
    cap[t] = w
    fee[t] = f
    link[u] = t
    

def add_edge(u, v, w, f):
    add(u, v, w, f)
    add(v, u, 0, -f)


def spfa(start, end):
    for i in range(MAXN):
        dist[i] = INF
        inq[i] = False
        flow[i] = 0
        pre[i] = -1
        prex[i] = -1
        
    q = collections.deque([start])
    dist[start] = 0
    flow[start] = INF
    while q:
        u = q.popleft()
        inq[u] = False
        i = link[u]
        while i >= 0:
            v = to[i]
            if cap[i] > 0 and dist[v] > dist[u] + fee[i]:
                dist[v] = dist[u] + fee[i]
                flow[v] = min(flow[u], cap[i])
                pre[v] = i
                prex[v] = u
                if not inq[v]:
                    inq[v] = True
                    q.append(v)
            i = nxt[i]
            
    return dist[end] < INF


def max_flow(start, end):
    ans = 0
    while spfa(start, end):
        # print(' '.join(map(str, cap[1:21])))
        ans += flow[end] * dist[end]
        u = end
        while u != start:
            cap[pre[u]] -= flow[end]
            cap[pre[u] ^ 1] += flow[end]
            # print(u, pre[u], end=' ')
            u = prex[u]
        # print()
        # print(ans)
    return ans


if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().strip().split()]
    p, m, f, n, s = map(int, input().strip().split())
    start, end = 0, 2*N+1
    for i, x in enumerate(A):
        day = i+1
        add_edge(start, day, x, 0) # 每天晚上从起点获得x条脏餐巾
        add_edge(day+N, end, x, 0) # 每天白天,向汇点提供x条干净的餐巾,流满时表示第day天的餐巾够用
    
    for i in range(1, N+1):
        if i + 1 <= N:
            add_edge(i, i+1, INF, 0) #每天晚上可以将脏餐巾留到第二天晚上
        if i + m <= N:
            add_edge(i, i+N+m, INF, f) #每天晚上可以送去快洗部,在地i+m天早上收到餐巾
        if i + n <= N:
            add_edge(i, i+N+n, INF, s) #每天晚上可以送去慢洗部,在地i+m天早上收到餐巾
        add_edge(start, i+N, INF, p) # 每天早上可以购买餐巾
    
    print(max_flow(start, end))
            
    
    
    
    