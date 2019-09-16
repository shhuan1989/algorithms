# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 9/11/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


#
# def consumption(N, K):
#     if K == 2:
#         return N+1
#     if K < 2:
#         return 0
#
#     conn = set()
#     for k in range(K):
#         for i in range(N):
#             u, v = i, (i+k) % N
#             if u > v:
#                 u, v = v, u
#             conn.add((u, v))
#     return len(conn)
#
#
# def capacity(N):
#     conn = set()
#     for i in range(N):
#         for j in range(i, N):
#             conn.add((i, j))
#     return len(conn)
#
# for n in range(2, 10):
#     print(n, capacity(n))
#
#
# for n in range(2, 10):
#     for k in range(2, n*n):
#         print(n, k, consumption(n, k))
#
#
#
#


def solve(N, M):
    cap = N * (N - 1) // 2 + N
    if N == 1:
        if M == 1:
            print(1)
        elif M == 0:
            print(0)
        else:
            print(-1)
    elif N == 2:
        if M == 1:
            print(1)
        elif 2 <= M <= 3:
            print(2)
        else:
            print(-1)
    elif M < N - 1 or M > cap:
        print(-1)
    elif N - 1 <= M <= N + 1:
        print(2)
    else:
        # N*(N-1)//2+N >= M
        K = 2 * M // N - 1 if (2 * M) % N == 0 else 2 * M // N
        K = max(K, 3)
        if K > N:
            print(-1)
        else:
            print(K)
    


# for N in range(10):
#     for M in range(N**2):
#         print('='*40)
#         print(N, M)
#         solve(N, M)

T = int(input())

for ti in range(T):
    N, M = map(int, input().split())
    solve(N, M)

        
        
        