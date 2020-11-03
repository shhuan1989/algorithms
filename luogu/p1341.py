# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/14

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



if __name__ == '__main__':
    # sys.stdin = open('P1341_2.in', 'r')
    N = int(input())
    
    
    chs = [chr(ord('A')+i) for i in range(26)] + [chr(ord('a')+i) for i in range(26)]
    # print(''.join(chs))
    vi = {v:i for i, v in enumerate(chs)}
    nchs = len(chs)
    deg = [0 for _ in range(nchs)]
    g = [[False for _ in range(nchs)] for _ in range(nchs)]
    
    for _ in range(N):
        line = input().strip()
        u, v = line[0], line[1]
        # print(u, v)
        u, v = vi[u], vi[v]
        deg[u] += 1
        deg[v] += 1
        g[u][v] = True
        g[v][u] = True
        
    odd = len([x for x in range(nchs) if deg[x] % 2 != 0])
    if odd > 0 and odd != 2:
        print('No Solution')
        exit(0)
        
    n = len([u for u in range(nchs) if deg[u] > 0])
    start = 0
    
    if odd == 2:
        for u in range(nchs):
            if deg[u] % 2 != 0:
                start = u
                break
    else:
        for u in range(nchs):
            if deg[u] != 0:
                start = u
                break
                
    vis = {start}
    q = [start]
    while q:
        u = q.pop()
        for v in range(nchs):
            if g[u][v] and v not in vis:
                vis.add(v)
                q.append(v)
    if len(vis) < n:
        print('No Solution')
        exit(0)
    
    
    ans = ['' for _ in range(N+1)]
    idx = [N]
    def dfs(u):
        for v in range(nchs):
            if g[u][v]:
                g[u][v] = False
                g[v][u] = False
                dfs(v)
        ans[idx[0]] = chs[u]
        idx[0] -= 1
    
    dfs(start)
    print(''.join(ans))
    