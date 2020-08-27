# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/5

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


INF = 10**9+7

if __name__ == '__main__':
    N, K, A, B, C = map(int, input().split())
    omap = [[]]
    for i in range(N):
        row = [0] + [int(x) for x in input().split()]
        omap.append(row)
    
    dp = [[[INF for _ in range(K+1)] for _ in range(N+1)] for _ in range(N+1)]
    inq = [[[False for _ in range(K + 1)] for _ in range(N + 1)] for _ in range(N + 1)]
    dp[1][1][K] = 0
    
    q = collections.deque([(1, 1, K)])
    inq[1][1][K] = True
    while q:
        r, c, k = q.popleft()
        inq[r][c][k] = False
        if k <= 0:
            continue
            
        
        for nr, nc, nd in [(r+1, c, 0), (r-1, c, B), (r, c+1, 0), (r, c-1, B)]:
            if 1 <= nr <= N and 1 <= nc <= N:
                if omap[nr][nc] == 1:
                    if dp[nr][nc][K] > dp[r][c][k] + nd + A:
                        dp[nr][nc][K] = dp[r][c][k] + nd + A
                        if not inq[nr][nc][K]:
                            inq[nr][nc][K] = True
                            q.append((nr, nc, K))
                else:
                    if dp[nr][nc][k-1] > dp[r][c][k] + nd:
                        dp[nr][nc][k-1] = dp[r][c][k] + nd
                        if not inq[nr][nc][k-1]:
                            inq[nr][nc][k-1] = True
                            q.append((nr, nc, k-1))
                    
                    if dp[nr][nc][K] > dp[r][c][k] + nd + A + C:
                        dp[nr][nc][K] = dp[r][c][k] + nd + A + C
                        if not inq[nr][nc][K]:
                            inq[nr][nc][K] = True
                            q.append((nr, nc, K))
    print(min(dp[N][N]))
        
    
    
    
    