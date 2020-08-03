# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/24

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        row = list(input().strip())
        A.append(row)
    
    sr, sc = 0, 0
    for r in range(N):
        for c in range(M):
            if A[r][c] == '*':
                A[r][c] = '.'
                sr, sc = r, c
    
    T = int(input())
    ops = []
    for ti in range(T):
        d = input().strip()
        if d == 'NORTH':
            ops.append((-1, 0))
        elif d == 'WEST':
            ops.append((0, -1))
        elif d == 'EAST':
            ops.append((0, 1))
        else:
            ops.append((1, 0))
            
    q = {(sr, sc)}
    for op in ops:
        nq = set()
        for x, y in q:
            t = 1
            while True:
                nx, ny = x + t * op[0], y + t * op[1]
                if 0 <= nx < N and 0 <= ny < M and A[nx][ny] == '.':
                    nq.add((nx, ny))
                else:
                    break
                t += 1
        q = nq
        
    for x, y in q:
        A[x][y] = '*'
    
    for row in A:
        print(''.join(row))
    
    