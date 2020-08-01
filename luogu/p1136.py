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
created by shhuan at 2020/7/18 14:18

"""


if __name__ == '__main__':

    N, K = map(int, input().split())
    S = input().strip()

    INF = 10**9+7
    dp = [[[-INF for _ in range(K+1)] for _ in range(K+1)] for _ in range(N+1)]
    ans = 0
    dp[0][0][0] = 0
    dp[1][0][0] = 0
    if S[0] == 'j':
        dp[1][1][0] = 0
    else:
        dp[1][0][1] = 0
    for i in range(2, N+1):
        a = S[i-2: i]
        for j in range(K+1):
            for k in range(K+1):
                v = dp[i-1][j][k]
                if a == 'jz':
                    v = max(v, dp[i-2][j][k] + 1)
                if a == 'jj' and j-1 >= 0:
                    v = max(v, dp[i-2][j-1][k] + 1)
                if a == 'zz' and k-1 >= 0:
                    v = max(v, dp[i-2][j][k-1] + 1)
                if a == 'zj' and j-1 >= 0 and k-1 >= 0:
                    v = max(v, dp[i-2][j-1][k-1] + 1)
                dp[i][j][k] = v

        ans = max(ans, max([dp[i][j][j] for j in range(K+1)]))

    print(ans)
