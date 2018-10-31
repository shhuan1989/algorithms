# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/30/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


N, M = map(int, input().split())

A = []
for i in range(N):
    A.append([int(x) for x in input()])
    


ans = [[float('inf')] * (N*M+1) for _ in range(2)]

rows = [[0 if i % 2 == 0 else 1 for i in range(M)], [1 if i % 2 == 0 else 0 for i in range(M)]]

b1 = [rows[i%2] for i in range(N)]
b2 = [rows[(i+1)%2] for i in range(N)]

boards = [b1, b2]
ans[0][1] = 0
ans[0][0] = 0
ans[1][1] = 0
ans[1][0] = 0
for ai, board in enumerate(boards):
    for c in range(M*N+1):
        for sr in range(N):
            for sc in range(M):
                reverted = 0
                for w in range(2, min(N-sr, M-sc)+1):
                    # print(w)
                    for r in range(sr, sr+w):
                        reverted += 1 if A[r][sc+w-1] != board[r][sc+w-1] else 0
                    for c in range(sc, sc+w):
                        reverted += 1 if A[sr+w-1][c] != board[sr+w-1][c] else 0
                    
                    ans[ai][w] = min(ans[ai][w], reverted)
                

Q = int(input())
qs = [int(x) for x in input().split()]
print(ans[0][:min(M, N)], ans[1][:min(M, N)])
for q in qs:
    if q >= M*N:
        print(min(M, N))
    else:
        i = bisect.bisect_right(ans[0], q)
        j = bisect.bisect_right(ans[1], q)
        print(min(i, j))