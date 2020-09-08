# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/1

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    # sys.stdin = open('p1285.in', 'r')
    N = int(input())
    g = collections.defaultdict(set)
    
    for i in range(1, N+1):
        conn = [int(x) for x in input().split()]
        g[i] = set(conn[:-1])
    
    rg = collections.defaultdict(list)
    for u in range(1, N+1):
        for v in range(u + 1, N+1):
            if u not in g[v] or v not in g[u]:
                rg[u].append(v)
                rg[v].append(u)
                
    groups = [-1 for _ in range(N+1)]
    colors = [-1 for _ in range(N+1)]
    gid = 0
    for i in range(1, N+1):
        if groups[i] > 0:
            continue
        gid += 1
        q = [(i, 0)]
        colors[i] = 0
        while q:
            u, c = q.pop()
            groups[u] = gid
            for v in rg[u]:
                if colors[v] == c:
                    print('No solution')
                    exit(0)
                colors[v] = c ^ 1
                if groups[v] < 0:
                    q.append((v, c ^ 1))
    
    # print(rg)
    # print(groups)
    
    ng = gid
    a = [0 for _ in range(ng + 1)]
    b = [0 for _ in range(ng + 1)]
    for i in range(1, N+1):
        if colors[i] == 0:
            a[groups[i]] += 1
        else:
            b[groups[i]] += 1
    
    dp = [[False for _ in range(2*N+1)] for _ in range(ng+1)]
    pre = [[-1 for _ in range(2 * N + 1)] for _ in range(ng + 1)]
    dp[0][N] = True
    for i in range(ng):
        cd = a[i+1] - b[i+1]
        for d in range(2 * N + 1):
            if not dp[i][d]:
                continue
            if d + cd < 2 * N + 1:
                dp[i+1][d+cd] = True
                pre[i+1][d+cd] = 0
            if d - cd >= 0:
                dp[i+1][d-cd] = True
                pre[i+1][d-cd] = 1
    
    diff = 0
    for d in range(N+1):
        if dp[ng][d + N]:
            diff = d + N
            break
        if dp[ng][N - d]:
            diff = N - d
            break
    
    
    i = ng
    swap = [False for _ in range(ng + 1)]
    while i > 0:
        d = a[i] - b[i]
        if pre[i][diff] == 1:
            swap[i] = True
            diff += d
        else:
            diff -= d
        
        i -= 1
    
    for i in range(1, N+1):
        if swap[groups[i]]:
            colors[i] ^= 1
    # print(ng)
    # print(colors)
    # print(swap)
    ga = [i for i in range(1, N + 1) if colors[i] == 0]
    gb = [i for i in range(1, N + 1) if colors[i] == 1]
    print('{} {}'.format(len(ga), ' '.join(map(str, ga))))
    print('{} {}'.format(len(gb), ' '.join(map(str, gb))))
    
    
    