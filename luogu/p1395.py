# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/16

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


if __name__ == '__main__':
    sys.setrecursionlimit(200000)
    N = int(input())
    E = [[] for _ in range(N+1)]
    
    for _ in range(N-1):
        u, v = map(int, input().split())
        E[u].append(v)
        E[v].append(u)
    
    
    # def dfs(u, p, d):
    #     ans = d
    #     for v in E[u]:
    #         if v != p:
    #             ans += dfs(v, u, d+1)
    #
    #     return ans
    
    
    @lru_cache(maxsize=None)
    def getchilds(u, p):
        ans = 1
        for v in E[u]:
            if v != p:
                ans += getchilds(v, u)
        return ans
        # count = 0
        # q = [u]
        # vis = [False for _ in range(N+1)]
        # if p > 0:
        #     vis[p] = True
        # vis[u] = True
        # while q:
        #     u = q.pop()
        #     for v in E[u]:
        #         if not vis[v]:
        #             vis[v] = True
        #             q.append(v)
        #     count += 1
        # return count
    
    
    def getinitdist():
        
        q = [1]
        d = 0
        td = 0
        vis = [False for _ in range(N+1)]
        vis[1] = True
        while q:
            nq = []
            td += d * len(q)
            for u in q:
                for v in E[u]:
                    if not vis[v]:
                        vis[v] = True
                        nq.append(v)
            d += 1
            q = nq
        
        return td
        
    
    
    dist = [0 for _ in range(N+1)]
    dist[1] = getinitdist()
    # print(dist)
    q = collections.deque([v for v in E[1]])
    parent = [-1 for _ in range(N+1)]
    parent[1] = 1
    for v in E[1]:
        parent[v] = 1
    while q:
        u = q.popleft()
        for v in E[u]:
            if parent[v] < 0:
                parent[v] = u
                q.append(v)
        
        c = getchilds(u, parent[u])
        dist[u] = dist[parent[u]] - c + (N-c)
    
    # print(dist)
    # print(min(dist[i] for i in range(1, N+1)))
    mindist = float('inf')
    mini = -1
    for i in range(1, N+1):
        if dist[i] < mindist:
            mindist = dist[i]
            mini = i
    
    print('{} {}'.format(mini, mindist))