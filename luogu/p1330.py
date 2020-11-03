# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/10

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


sys.setrecursionlimit(200000)

if __name__ == '__main__':
    # sys.stdin = open('P1330_9.in', 'r')
    N, M = map(int, input().split())
    g = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
        
    color = [-1 for _ in range(N+1)]
    tim = [-1 for _ in range(N+1)]
    
    # def dfs(u, p, c, t):
    #     color[u] = c
    #     tim[u] = t
    #     for v in g[u]:
    #         if v != p:
    #             if color[v] >= 0 and color[v] != c ^ 1:
    #                 print('Impossible')
    #                 exit(0)
    #             dfs(v, u, c ^ 1, t)
    
    
    def bfs(u, c, t):
        q = [(u, -1, c)]
        while q:
            u, p, c = q.pop()
            color[u] = c
            tim[u] = t
            for v in g[u]:
                if v == p:
                    continue
                if color[v] >= 0 and color[v] != c ^ 1:
                    print('Impossible')
                    exit(0)
                q.append((v, u, c ^ 1))
    
    ab = []
    ans = 0
    t = 1
    for i in range(1, N+1):
        if color[i] < 0:
            t += 1
            bfs(i, 0, t)
            a = len([x for i, x in enumerate(color) if x == 1 and tim[i] == t])
            b = len([x for i, x in enumerate(color) if x == 0 and tim[i] == t])
            if a + b > 1:
                ab.append((a, b))
            ans += min(a, b)
    
    # tc = collections.defaultdict(list)
    # for i in range(1, N+1):
    #     tc[tim[i]].append(i)
    
    # print(tc)
    # print(ab)
    print(ans)