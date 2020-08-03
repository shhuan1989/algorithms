# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/29

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    sys.stdin = open('p1231.in', 'r')
    N1, N2, N3 = map(int, input().strip().split())
    
    MAXN, MAXM = 4*10**4+5, 10**6+5
    tot = [1]
    link = [-1 for _ in range(MAXN)]
    vertex = [-1 for _ in range(MAXM)]
    cap = [-1 for _ in range(MAXM)]
    nxt = [-1 for _ in range(MAXM)]
    level = [-1 for _ in range(MAXN)]
    curindex = [-1 for _ in range(MAXN)]
    
    def id(p, x):
        if p == 1:
            return x
        elif p == 2:
            return N2 + x
        elif p == 3:
            return N1 + N2 + x
        elif p == 4:
            return N1 + N1 + N2 + x
        
    def add(u, v, w):
        tot[0] += 1
        i = tot[0]
        vertex[i] = v
        nxt[i] = link[u]
        link[u] = i
        cap[i] = w
    
    def add_edge(u, v, w):
        add(u, v, w)
        add(v, u, 0)
    
    def bfs(s, t):
        for i in range(MAXN):
            level[i] = 0
        
        q = collections.deque([s])
        level[s] = 1
        while q:
            u = q.popleft()
            i = link[u]
            while i > 0:
                v = vertex[i]
                if level[v] <= 0 and cap[i] > 0:
                    level[v] = level[u] + 1
                    q.append(v)
                i = nxt[i]
        
        return level[t] > 0
    
    def dfs(u, t, flow, path):
        if u == t:
            if flow > 0:
                print(flow, path)
            return flow
        
        ans = 0
        i = curindex[u]
        while i > 0 and ans < flow:
            curindex[u] = i
            v = vertex[i]
            if cap[i] > 0 and level[v] == level[u] + 1:
                x = dfs(v, t, min(cap[i], flow-ans), path + [v])
                if x > 0:
                    cap[i] -= x
                    cap[i^1] += x
                    ans += x
            i = nxt[i]
        if ans < flow:
            level[u] = -1
        
        return ans
    
    def dinic(s, t):
        ans = 0
        while bfs(s, t):
            for i in range(MAXN):
                curindex[i] = link[i]
            while True:
                x = dfs(s, t, 1 << 30, [s])
                if x > 0:
                    ans += x
                else:
                    break
        return ans
    
    def findlink(u):
        i = link[u]
        x = []
        while i > 0:
            if cap[i] > 0:
                x.append(vertex[i])
            i = nxt[i]
        return x
    
    M1 = int(input())
    for i in range(M1):
        # print(input())
        x, y = map(int, input().strip().split())
        add_edge(id(1, y), id(2, x), 1)
    
    M2 = int(input())
    for i in range(M2):
        x, y = map(int, input().strip().split())
        add_edge(id(3, x), id(4, y), 1)
    
    for i in range(1, N1+1):
        add_edge(id(2, i), id(3, i), 1)
    
    start, end = 0, N1 + N1 + N2 + N3 + 1
    for i in range(1, N2+1):
        add_edge(start, id(1, i), 1)
    for i in range(1, N3+1):
        add_edge(id(4, i), end, 1)
    
    print(dinic(start, end))
    
    # for i in range(end+1):
    #     print(i, ' '.join(map(str, findlink(i))))
        
        
    