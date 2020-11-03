# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/14

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
    
    chess = [
        [
            ['#', '#', '#'],
            ['.', '#', '.'],
            ['.', '#', '.'],
        ],
        [
            ['.', '.', '#'],
            ['#', '#', '#'],
            ['.', '.', '#'],
        ],
        [
            ['#', '.', '.'],
            ['#', '#', '#'],
            ['#', '.', '.'],
        ],
        [
            ['.', '#', '.'],
            ['.', '#', '.'],
            ['#', '#', '#'],
        ]
    ]
    
    A = [['.' for _ in range(M)] for _ in range(N)]
    
    
    def canplace(x, y, p):
        if x + 3 > N or y + 3 > M:
            return False
        
        for r in range(x, x+3):
            for c in range(y, y+3):
                if A[r][c] != '.' and chess[p][r-x][c-y] == '#':
                    return False
                
        return True
    
    def place(x, y, p):
        for r in range(x, x + 3):
            for c in range(y, y + 3):
                if chess[p][r - x][c - y] == '#':
                    A[r][c] = '#'
    
    def unplace(x, y, p):
        for r in range(x, x + 3):
            for c in range(y, y + 3):
                if chess[p][r - x][c - y] == '#':
                    A[r][c] = '.'
    
    maxp = [[-1 for _ in range(M)] for _ in range(N)]
    ans = [0]
    
    def dfs(x, y):
        global maxp
        if x >= N - 2:
            return 0
        
        if maxp[x][y] >= 0 and maxp[x][y] + 1 < ans[0]:
            return 0
        
        nx = x if y + 1 < M else x + 1
        ny = y + 1 if y + 1 < M else 0
        ret = 0
        for p in range(4):
            if canplace(x, y, p):
                place(x, y, p)
                ret = max(ret, 1 + dfs(nx, ny))
                unplace(x, y, p)
        
        ret = max(ret, dfs(nx, ny))
        
        maxp[x][y] = ret
        # print(x, y, ret)
        # print(maxp)
        return ret
    
    ans = dfs(0, 0)
    print(maxp)
    print(ans)
    
    