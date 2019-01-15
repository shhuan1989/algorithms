# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/11/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


# def chech(matrix):
#     n, m = len(matrix), len(matrix[0])
#
#     for r in range(n):
#         for c in range(n):
#             nbs = [(nr, nc) for nr, nc in [(r - 1, c), (r+1, c), (r, c+1), (r, c - 1)] if 0 <= nr < n and 0 <= nc < m]
#
#             if len(nbs) != len({matrix[nr][nc] for nr, nc in nbs}):
#                 return False
#
#     return True
    
    

def solve(N, M):
    A = [[0 for _ in range(M)] for _ in range(N)]
    
    maxV = 0
    for r in range(N):
        for c in range(M):
            v = A[r][c]
            nbs = [(nr, nc) for nr, nc in [(r-1, c), (r, c-1)] if 0 <= nr < N and 0 <= nc < M]
            nbnbs = []
            for nr, nc in nbs:
                nbnbs.extend([(x, y) for x, y in [(nr+1, nc), (nr-1, nc), (nr, nc+1), (nr, nc-1)] if 0 <= x < N and 0 <= y < M])
            
            nbvs = {A[nr][nc] for nr, nc in nbnbs}
            v = 1
            while v in nbvs:
                v += 1
            A[r][c] = v
            maxV = max(v, maxV)
    
    return maxV, A


# for n in range(1, 50):
#     for m in range(1, 50):
#         print(n, m, solve(n, m)[0])


T = int(input())
for ti in range(T):
    N, M = map(int, input().split())
    # print(solve(N, M))
    V, A = solve(N, M)
    print(V)
    print('\n'.join([' '.join(map(str, row)) for row in A]))
    