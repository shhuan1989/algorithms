# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-05-07

"""

import collections
import time
import os
import sys
import bisect
import heapq





T = int(input())
for ti in range(T):
    N = int(input())
    A = [[False for _ in range(N)] for _ in range(N)]
    
    rs = [[] for _ in range(N)]
    cs = [[] for _ in range(N)]
    
    c = 0
    # for c in range(0, 2*N, 10):
    d = 2
    count = 0
    while c < 2 * N + 10:
        for r in range(c+1):
            if r < N and c - r < N:
                A[r][c-r] = True
                count += 1
                rs[c-r].append(r)
                cs[r].append(c)
        c += d
        # d += 1
        if c >= N and d > 3:
            # d -= 2
            break
        else:
            d += 1
            # print(d)
        #     # pass
        # d = c % 2 + 2
    # print(count)
    # for dx, dy in [(1, 1), (2, 1), (3, 1)]
    
    # count = 0
    # dx, dy = 1, 1
    # # for dx in range( N):
    # for dy in range(1, N):
    #     r, c = 0, 0
    #     while r < N and c < N:
    #         # print(r, c)
    #         A[r][c] = True
    #         r += dx
    #         c += dy
    #         count += 1
    #
    # print(count)
    #
    
    # for r in range(N):
    #     for c in range(N):
    #         for r1 in rs[c]:
    #             for c1 in cs[r]:
    #                 if A[r1][c1]:
    #                     print((r, c), (r1, c1), (r, c1), (r1, c))
    
    A[0][0] = False
    points = []
    for r in range(N):
        for c in range(N):
            if A[r][c]:
                for r1 in range(r+1, N):
                    for c1 in range(c+1, N):
                        if A[r1][c1] and A[r][c1] and A[r1][c]:
                            print(r, c, r1, c1)
                            points.extend([()])
    
    
    
    for row in A:
        print(''.join(['O' if v else ' ' for v in row]))