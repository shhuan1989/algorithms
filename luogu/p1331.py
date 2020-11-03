# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/10

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    # sys.stdin = open('P1331_1.in', 'r')
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        row = list(input().strip())
        A.append(row)
    
    number = [[0 for _ in range(M)] for _ in range(N)]
    id = 0
    lefttop = {}
    rightbottom = {}
    for r in range(N):
        for c in range(M):
            if A[r][c] == '#':
                if number[r][c] == 0:
                    id += 1
                    number[r][c] = id
                    lefttop[id] = (r, c)
                    rightbottom[id] = (r, c)
                    q = [(r, c)]
                    while q:
                        x, y = q.pop()
                        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                            if 0 <= nx < N and 0 <= ny < M and A[nx][ny] == '#' and number[nx][ny] == 0:
                                number[nx][ny] = id
                                q.append((nx, ny))
                                rbx, rby = rightbottom[id]
                                ltx, lty = lefttop[id]
                                rightbottom[id] = (max(rbx, nx), max(rby, ny))
                                lefttop[id] = (min(ltx, nx), min(lty, ny))
                                
    
    # for row in number:
    #     print(row)
    
    for i in range(1, id+1):
        x0, y0 = lefttop[i]
        x1, y1 = rightbottom[i]
        for r in range(x0, x1+1):
            for c in range(y0, y1+1):
                if number[r][c] != i:
                    print('Bad placement.')
                    exit(0)
    
    print('There are {} ships.'.format(id))