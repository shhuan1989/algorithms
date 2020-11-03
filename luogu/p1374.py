# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/27

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


import math

from functools import lru_cache
if __name__ == '__main__':
    N, M, S, D = map(int, input().split())
    A = []
    for _ in range(N):
        row = [int(x) for x in input().strip()]
        A.append(row)
    
    sx, sy, ex, ey = map(int, input().strip().split())
    sx -= 1
    sy -= 1
    ex -= 1
    ey -= 1
    movea = [int(x) for x in input().strip()]
    moveb = [int(x) for x in input().strip()]
    
    
    dxy = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def check(x, y):
        return 0 <= x < N and 0 <= y < M and A[x][y] == 0
        
        
    def getdist(x1, y1, x2, y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    def getnextsar(x, y, t):
        move = movea[t % len(movea)]
        dx, dy = dxy[move]
        nx, ny = x + dx, y + dy
        return (nx, ny) if check(nx, ny) else (x, y)
    
    def getnextevil(x, y, t):
        move = moveb[t % len(moveb)]
        dx, dy = dxy[move]
        nx, ny = x + dx, y + dy
        return (nx, ny) if check(nx, ny) else (x, y)
    
    
    # bx, by = sx, sy
    # for t in range(10):
    #     bx, by = getnextsar(bx, by, t)
    #     print(bx, by)
        
    
    q = collections.deque([(0, sx, sy, sx, sy, ex, ey, 0)])
    # vis = {(0, 0, sx, sy, sx, sy, ex, ey)}
    while q:
        t, ax, ay, bx, by, cx, cy, ot = q.popleft()
        if ax == cx and ay == cy:
            print(t)
            break
        # if t == 3:
        #     print(ax, ay, bx, by, cx, cy, ot)
        # if t > 3:
        #     break
        # if ot > S:
        #     continue
        bx, by = getnextsar(bx, by, t)
        cx, cy = getnextevil(cx, cy, t)
        q.append((t+1, ax, ay, bx, by, cx, cy, 0 if getdist(ax, ay, bx, by) < D else ot + 1))
        for nx, ny in [(ax+1, ay), (ax-1, ay), (ax, ay+1), (ax, ay-1)]:
            if check(nx, ny):
                q.append((t+1, nx, ny, bx, by, cx, cy, 0 if getdist(nx, ny, bx, by) < D else ot + 1))
        