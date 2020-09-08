# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/31

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N = int(input())
    A = []
    
    for _ in range(N):
        y0, x0, y1, x1, c = map(int, input().split())
        A.append((y0, x0, y1, x1, c))
    
    def attop(a, b):
        return A[a][2] == A[b][0] and (A[b][1] <= A[a][1] <= A[b][3] or A[b][1] <= A[a][3] <= A[b][3])
    
    g = collections.defaultdict(list)
    pre = collections.defaultdict(list)
    ind = [0 for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if attop(i, j):
                g[i].append(j)
                pre[j].append(i)
                ind[j] += 1
    
    INF = 1000
    C = 21
    dp = [[INF for _ in range(C)] for _ in range(1 << N)]
    q = collections.deque([(1 << i, A[i][-1]) for i in range(N) if ind[i] == 0])
    for p, c in q:
        dp[p][c] = 1
    while q:
        paint, prec = q.popleft()
        for i in range(N):
            if paint & (1 << i) > 0:
                continue
            if any([paint & (1 << j) == 0 for j in pre[i]]):
                continue
    
            c = A[i][-1]
            step = dp[paint][prec] + (1 if prec != c else 0)
            npaint = paint | (1 << i)
            if step < dp[npaint][c]:
                dp[npaint][c] = step
                q.append((npaint, c))
    
    print(min(dp[(1 << N) - 1]))