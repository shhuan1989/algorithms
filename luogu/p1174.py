# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/7/21 21:12

"""


if __name__ == '__main__':
    N, M, K = map(int, input().split())

    A = [[] for _ in range(M)]
    B = [[] for _ in range(M)]
    for i in range(N):
        line = input().strip().split()
        row = [int(x) for x in line[0:2*M:2]]
        for j in range(M):
            A[j].append(row[j])
        row = [x == 'Y' for x in line[1:2*M:2]]
        for j in range(M):
            B[j].append(row[j])

    down = [[0 for _ in range(N+1)] for _ in range(M)]
    downb = [[0 for _ in range(N+1)] for _ in range(M)]
    for i in range(N-1, -1, -1):
        for j in range(M):
            down[j][i] += down[j][i+1] + A[j][i]
            downb[j][i] += downb[j][i+1] + B[j][i]

    bcount = sum([downb[i][0] for i in range(M)])
    bc = [0]
    for i in range(M):
        bc.append(bc[-1] + downb[i][0])
    dp = [[[float('-inf') for _ in range(bcount+1)] for _ in range((i+1)*N+1)] for i in range(M)]
    for j in range(N+1):
        dp[0][j][downb[0][N-j]] = down[0][N-j]

    ans = 0
    add = downb[0][0]
    for i in range(1, M):
        add += downb[i][0]
        for j in range(min((i+1)*N, add+K) + 1):
            for k in range(add+1):
                for l in range(min(N, j)+1):
                    if k - downb[i][N-l] < 0 or k - downb[i][N-l] >= len(dp[i-1][j-l]):
                        break
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-l][k-downb[i][N-l]] + down[i][N-l])
                if j <= K+k:
                    # print(i, j, k, dp[i][j][k])
                    ans = max(ans, dp[i][j][k])

    print(ans)