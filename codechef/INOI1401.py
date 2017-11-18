# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/17 10:26

"""

R, C, D = map(int, input().split())

D += 1
A = []
for i in range(R):
    A.append([int(x) for x in input().split()])


# subtask 1
if A[0][0] == 0:
    print(0)
    exit(0)

if R*C == 1:
    print(1)
    exit(0)
# DP = [[0 for _ in range(C)] for _ in range(R)]
# DP[0][0] = 1
#
#
# for r in range(R):
#     for c in range(C):
#         if not A[r][c]:
#             continue
#         if c > 0:
#             DP[r][c] += DP[r][c-1]
#         if r > 0:
#             DP[r][c] += DP[r-1][c]
#
# print(DP[R-1][C-1])

LR = [[[0 for _ in range(D)] for _ in range(C)] for _ in range(R)] # left -> right LR[r][c][d] means at position r, c; d steps from left to right
UD = [[[0 for _ in range(D)] for _ in range(C)] for _ in range(R)] # up -> down

LR[0][0][0] = 1
UD[0][0][0] = 1

for r in range(R):
    for c in range(C):
        if r == 0 and c == 0:
            continue
        if A[r][c]:
            if c > 0:
                LR[r][c][1] += sum(UD[r][c-1][1:]) # up-down => left-right
                for dh in range(1, D): # left -> right
                    LR[r][c][dh] += LR[r][c-1][dh-1]
            if r > 0:
                UD[r][c][1] += sum(LR[r-1][c][1:]) # left-right => up-down
                for dv in range(1, D): # up-down
                    UD[r][c][dv] += UD[r-1][c][dv-1]

print(sum(LR[R-1][C-1]) + sum(UD[R-1][C-1]))