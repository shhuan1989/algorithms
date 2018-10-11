# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/10/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


C = [
    ['#', '#', '#'],
    ['#', '', '#'],
    ['#', '#', '#'],
]

N, M = map(int, input().split())

res = [['' for _ in range(M)] for _ in range(N)]

A = []
for i in range(N):
    A.append([x for x in input()])
    
    
for i in range(N-2):
    for j in range(M-2):
        
        edge = []
        for x in range(3):
            for y in range(3):
                if not (x==1 and y == 1):
                    edge.append((i + x, j + y))
        
        if all(A[r][c]=='#' for (r, c) in edge):
            for r, c in edge:
                res[r][c] = '#'

for row in res:
    print(row)
    
if res == A:
    print('YES')
else:
    print('NO')