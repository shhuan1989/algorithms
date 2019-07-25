# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-07-19

"""

import collections
import time
import os
import sys
import bisect
import heapq
import math

line = input()

L = len(line)

sqrtl = math.sqrt(L)

low, high = int(math.floor(sqrtl)), int(math.ceil(sqrtl))

area = float('inf')
row, col = 0, 0

for r in range(low, high + 1):
    for c in range(row, high+1):
        if L <= r * c < area:
            area = r * c
            row, col = r, c


matrix = [line[i: i+col] for i in range(0, L, col)]

ans = []
for c in range(col):
    ans.append(''.join([matrix[r][c] if c < len(matrix[r]) else '' for r in range(row)]))

print(' '.join(ans))
