# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/17

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

DX = [0, -1, 0, 1]
DY = [1, 0, -1, 0]


def canmoveto(N, M, A, x, y):
    if x <= 0 or x >= N or y <= 0 or y >= M:
        return False
    
    for r, c in [(x, y), (x, y + 1), (x + 1, y), (x + 1, y + 1)]:
        if 0 < r <= N and 0 < c <= M and A[r][c] == 1:
            return False
    
    return True


def solve(N, M, A, sx, sy, tx, ty, direction):
    q = [(0, sx, sy, direction)]
    vis = {(sx, sy, direction)}
    heapq.heapify(q)
    pre = {}
    while q:
        t, x, y, d = heapq.heappop(q)
        # print(t, x, y, d)
        if x == tx and y == ty:
            # dd = ['→', '↑', '←', '↓']
            # ans = [(x, y, d)]
            # while True:
            #     key = ans[-1]
            #     if key not in pre:
            #         break
            #     ans.append(pre[key])
            #
            # print([(r, c, dd[d]) for r, c, d in ans[::-1]])
            
            return t
        
        # move
        for s in range(1, 4):
            nx, ny = x + s * DX[d], y + s * DY[d]
            if canmoveto(N, M, A, nx, ny):
                key = (nx, ny, d)
                if key not in vis:
                    vis.add(key)
                    pre[key] = (x, y, d)
                    heapq.heappush(q, (t + 1, nx, ny, d))
            else:
                break
        
        # turn left
        nd = (d + 3) % 4
        key = (x, y, nd)
        if key not in vis:
            vis.add(key)
            pre[key] = (x, y, d)
            heapq.heappush(q, (t + 1, x, y, nd))
        
        # turn right
        nd = (d + 1) % 4
        key = (x, y, nd)
        if key not in vis:
            vis.add(key)
            pre[key] = (x, y, d)
            heapq.heappush(q, (t + 1, x, y, nd))
    
    return -1


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    A = [[0 for _ in range(M + 1)]]
    for i in range(N):
        row = [0] + [int(x) for x in input().strip().split()]
        A.append(row)
    
    sx, sy, tx, ty, direction = input().strip().split()
    sx, sy, tx, ty = [int(x) for x in [sx, sy, tx, ty]]
    di = {
        "E": 0,
        "N": 1,
        "W": 2,
        "S": 3
    }
    
    print(solve(N, M, A, sx, sy, tx, ty, di[direction]))

