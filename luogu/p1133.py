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
created by shhuan at 2020/7/17 23:51

"""



if __name__ == '__main__':
    N = int(input())

    A = []
    for i in range(N):
        a, b, c = map(int, input().split())
        A.append((a, b, c))

    ans = 0
    for s in range(3):
        for sk in range(2):
            dp = [[[float('-inf') for _ in range(2)] for _ in range(3)] for _ in range(N + 1)]
            dp[0][s][sk] = A[0][s]
            for i in range(N-1):
                for j in range(3):
                    for k in range(j+1, 3):
                        dp[i+1][k][1] = max(dp[i+1][k][1], dp[i][j][0] + A[i+1][k])

                    for k in range(j):
                        dp[i+1][k][0] = max(dp[i+1][k][0], dp[i][j][1] + A[i+1][k])
            if sk == 0:
                ans = max(ans, max([dp[N-1][i][1] for i in range(s+1, 3)] or [0]))
            else:
                ans = max(ans, max([dp[N-1][i][0] for i in range(s)] or [0]))

    print(ans)