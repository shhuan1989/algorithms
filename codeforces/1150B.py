# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-04-30

"""

import collections
import time
import os
import sys
import bisect
import heapq


N = int(input())

A = []


for i in range(N):
    row = [True if x != '#' else False for x in list(input())]
    A.append(row)
    
    
for r in range(N):
    for c in range(N):
        if A[r][c]:
            for nr, nc in [(r+1, c), (r+1, c-1), (r+1, c+1), (r+2, c)]:
                if 0 <= nr < N and 0 <= nc < N and A[nr][nc]:
                    A[nr][nc] = False
                else:
                    print('NO')
                    exit(0)
                    
print('YES')
        