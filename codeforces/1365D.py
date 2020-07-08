# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/9

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, M, A):
    good = 0
    for r in range(N):
        for c in range(M):
            if A[r][c] == 'B':
                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= nr < N and 0 <= nc < M:
                        if A[nr][nc] == 'G':
                            return False
                        if A[nr][nc] == '.':
                            A[nr][nc] = '#'
            elif A[r][c] == 'G':
                good += 1
    
    if A[N-1][M-1] == '#':
        return good == 0
    
    INF = M * N + 1
    dist = [[INF for _ in range(M)] for _ in range(N)]
    dist[N-1][M-1] = 0
    q = collections.deque([(N-1, M-1)])
    while q:
        r, c = q.popleft()
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if 0 <= nr < N and 0 <= nc < M and A[nr][nc] != '#' and dist[r][c] + 1 < dist[nr][nc]:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    
    for r in range(N):
        for c in range(M):
            if A[r][c] == 'G' and dist[r][c] >= INF:
                return False
            if A[r][c] == 'B' and dist[r][c] < INF:
                return False
            
    return True


T = int(input())
ans = []
for ti in range(T):
    N, M = map(int, input().split())
    A = []
    for r in range(N):
        A.append(list(input()))
    ans.append(solve(N, M, A))

print('\n'.join(['YES' if v else 'NO' for v in ans]))
