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
A = []
for i in range(N):
    A.append([x for x in input()])

# N, M = 1000, 1000
#
# A = [['.' if random.randint(0, 10) > 7 else '#' for _ in range(M)] for _ in range(N)]

t0 = time.time()

res = [['.' for _ in range(M)] for _ in range(N)]
ds = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]

for i in range(N - 2):
    for j in range(M - 2):
        if all(A[i+r][j+c] == '#' for (r, c) in ds):
            for r, c in ds:
                res[i+r][j+c] = '#'
        elif A[i][j] != res[i][j]:
            print('NO')
            # print(time.time() - t0)
            exit(0)
#
# for row in res:
#     print(''.join(row))

if res == A:
    print('YES')
else:
    print('NO')
    
# print(time.time() - t0)