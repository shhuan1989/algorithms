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

if __name__ == '__main__':
    N, M, P = map(int, input().split())
    K = int(input())
    gate = {}
    wall = set()
    for i in range(K):
        x1, y1, x2, y2, g = map(int, input().strip().split())
        if g > 0:
            gate[(x1, y1, x2, y2)] = g
        else:
            wall.add((x1, y1, x2, y2))
            wall.add((x2, y2, x1, y1))
    
    S = int(input())
    keys = collections.defaultdict(list)
    for i in range(S):
        x, y, k = map(int, input().split())
        keys[x, y].append(k)
    
    O = 2 ** (S+1)
    INF = 10**9 + 7
    dp = [[[INF for _ in range(O)] for _ in range(M+1)] for _ in range(N+1)]
    # prex = [[-1for _ in range(M+1)] for _ in range(N+1)]
    # prey = [[-1 for _ in range(M + 1)] for _ in range(N + 1)]
    
    
    def toid(x, y):
        return (x-1)*M + y
    
    s = 0
    for k in keys[1, 1]:
        s |= 1 << k
    dp[1][1][s] = 0
    q = collections.deque([(1, 1, s)])
    # inq = [False for _ in range(N*M+1)]
    
    while q:
        x, y, s = q.popleft()
        # inq[toid(x, y)] = False
        # print(x, y, s, dp[x][y][s])
        
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 < nx <= N and 0 < ny <= M:
                w = (x, y, nx, ny)
                if w in wall:
                    continue
                
                if w in gate and s & (1 << gate[w]) == 0:
                    continue
                
                ns = s
                for k in keys[nx, ny]:
                    ns |= 1 << k
                
                if dp[x][y][s] + 1 < dp[nx][ny][ns]:
                    dp[nx][ny][ns] = dp[x][y][s] + 1
                    q.append((nx, ny, ns))
                    # prex[nx][ny] = x
                    # prey[nx][ny] = y
    
    ans = min(dp[N][M])
    print(ans if ans < INF else -1)
    
                    
                
                
        
        
    