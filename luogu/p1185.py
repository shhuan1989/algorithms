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



def merge(t1, t2):
    
    n, m = len(t1), len(t1[0])
    
    if m == 1:
        return [
            ['o', ' ', ' ', ' ', 'o'],
            [' ', '/', ' ', '\\', ' '],
            [' ', ' ', 'o', ' ', ' '],
        ]
    
    t = [[' ' for _ in range(m*2+1)] for _ in range(n)]
    
    # left
    for r in range(n):
        for c in range(m):
            t[r][c] = t1[r][c]
            t[r][c+m+1] = t2[r][c]
    
    
    l, r = m//2 + 1, m//2+m
    while l < r:
        row = [' ' for _ in range(m*2+1)]
        row[l] = '/'
        row[r] = '\\'
        t.append(row)
        l += 1
        r -= 1
    row = [' ' for _ in range(m * 2 + 1)]
    row[l] = 'o'
    t.append(row)
        
    return t
    
    
    
def shear(t, l, c):
    n, m = len(t), len(t[0])
    v = 0
    for i in range(m):
        v += 1 if t[l][i] in ['o', 'x'] else 0
        if v == c:
            # up
            t[l][i] = 'x'
            q = [(l-1, i-1), (l-1, i+1)]
            while q:
                x, y = q.pop()
                if x >= 0 and 0 <= y < m:
                    if t[x][y] in ['o', 'x']:
                        q.append((x-1, y-1))
                        q.append((x-1, y+1))
                    elif t[x][y] == '\\':
                        q.append((x-1, y+1))
                    elif t[x][y] == '/':
                        q.append((x-1, y-1))

                    t[x][y] = ' '
            # down
            q = [(l+1, i-1), (l+1, i+1)]
            while q:
                x, y = q.pop()
                if 0 <= x < n and 0 <= y < m:
                    if t[x][y] == '\\':
                        t[x][y] = ' '
                        q.append((x+1, y-1))
                    elif t[x][y] == '/':
                        t[x][y] = ' '
                        q.append((x+1, y+1))
            
            break

def solve(N, remove):
    
    t = [['o']]
    level = [0]
    for i in range(N-1):
        t = merge(t, t)
        level.append(len(t)-1)
        
        # for row in t1:
        #     print(row)
    
    for l, c in remove:
        shear(t, level[len(level)-l], c)
    
    for r in range(len(t)):
        for c in range(len(t[0])):
            if t[r][c] == 'x':
                t[r][c] = ' '
    
    for row in reversed(t):
        print(''.join(row))
    

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    A = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append((a, b))
    solve(N, A)