# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/7

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    M, N = map(int, input().split())
    A = []
    for _ in range(N):
        row = [int(x) for x in input().split()]
        A.append(row)
    
    vis = [[[False for _ in range(8)] for _ in range(M)] for _ in range(N)]
    
    # dxy = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        
    q = collections.deque([(0, 0, 0, -1)])
    while q:
        x, y, step, d = q.popleft()
        if x == N-1 and y == M-1:
            print(step)
            exit(0)
        for nd in range(8):
            if nd == d:
                continue
            
            m = A[x][y]
            nx, ny = x + m * dx[nd], y + m * dy[nd]
            if 0 < nx < N and 0 < ny < M and not vis[nx][ny][nd]:
                vis[nx][ny][nd] = True
                q.append((nx, ny, step + 1, nd))
    
    print('NEVER')
    
    
    