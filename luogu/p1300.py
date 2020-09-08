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
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        row = list(input().strip())
        A.append(row)
    
    dmap = {
        'E': 0,
        'S': 1,
        'W': 2,
        'N': 3
    }
    
    sx, sy, sd = -1, -1, -1
    ex, ey = -1, -1
    for r in range(H):
        for c in range(W):
            if A[r][c] in dmap:
                sx, sy, sd = r, c, dmap[A[r][c]]
                # A[r][c] = '.'
            if A[r][c] == 'F':
                # A[r][c] = '.'
                ex, ey = r, c
    
    INF = 10 ** 9 + 7
    dist = [[[INF for _ in range(4)] for _ in range(W)] for _ in range(H)]
    pre = [[[(-1, -1, -1) for _ in range(4)] for _ in range(W)] for _ in range(H)]
    dist[sx][sy][sd] = 0
    
    q = collections.deque([(sx, sy, sd)])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        x, y, d = q.popleft()
        cost = dist[x][y][d]
        nx, ny = x + dx[d], y + dy[d]
        
        # go straight
        if 0 <= nx < H and 0 <= ny < W and A[nx][ny] != '.' and dist[nx][ny][d] > cost:
            dist[nx][ny][d] = cost
            pre[nx][ny][d] = (x, y, d)
            q.append((nx, ny, d))
        move = 0 <= nx < H and 0 <= ny < W and A[nx][ny] != '.'
        
        # turn left
        nd = (d + 3) % 4
        ncost = cost + 1
        nx, ny = x + dx[nd], y + dy[nd]
        if 0 <= nx < H and 0 <= ny < W and A[nx][ny] != '.' and dist[nx][ny][nd] > ncost:
            pre[nx][ny][nd] = (x, y, d)
            dist[nx][ny][nd] = ncost
            q.append((nx, ny, nd))
        
        if not move:
            move = 0 <= nx < H and 0 <= ny < W and A[nx][ny] != '.'
        
        
        # turn right
        nd = (d + 1) % 4
        ncost = cost + 5
        nx, ny = x + dx[nd], y + dy[nd]
        if 0 <= nx < H and 0 <= ny < W and A[nx][ny] != '.' and dist[nx][ny][nd] > ncost:
            pre[nx][ny][nd] = (x, y, d)
            dist[nx][ny][nd] = ncost
            q.append((nx, ny, nd))
        
        if not move:
            move = 0 <= nx < H and 0 <= ny < W and A[nx][ny] != '.'
        
        if not move:
            nd = (d + 2) % 4
            ncost = cost + 10
            nx, ny = x + dx[nd], y + dy[nd]
            if 0 <= nx < H and 0 <= ny < W and A[nx][ny] != '.' and dist[nx][ny][nd] > ncost:
                pre[nx][ny][nd] = (x, y, d)
                dist[nx][ny][nd] = ncost
                q.append((nx, ny, nd))

    print(min(dist[ex][ey]))
    
    # ans = INF
    # di = -1
    # for i in range(4):
    #     if dist[ex][ey][i] < ans:
    #         di = i
    #         ans = dist[ex][ey][i]
    
    # path = [(ex, ey, di)]
    # x, y, i = ex, ey, di
    # while x >= 0:
    #     x, y, i = pre[x][y][i]
    #     path.append((x, y, i))
    #
    # print(path[::-1])
    
    
    
    
        
        
        
            
    