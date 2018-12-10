# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/9 20:36

"""


N = int(input())
A = [int(x) for x in input().split()]


# dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
# for i in range(N+1):
#     dp[i][0] = 1
# for i in range(1, N+1):
#     for j in range(1, min(i, N) + 1):
#         dp[i][j] += dp[i-1][j]
#         if A[i-1] % j == 0:
#             dp[i][j] += dp[i-1][j-1]

def divisor(val, maxd):
    ans = []
    for i in range(min(int(math.sqrt(val))+1, maxd), 0, -1):
        if val % i == 0:
            ans.append(i)
    return ans

dp = [0] * (N+1)
dp[0] = 1
for i in range(1, N+1):
    for j in divisor(A[i-1], min(i, N)):
        dp[j] += dp[j-1]

ans = sum(dp) - 1
print(ans)