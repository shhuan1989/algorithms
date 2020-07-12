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
created by shhuan at 2020/7/9 21:29

"""


def solve(N, M):
    dp = [[0 for _ in range(M + 1)] for _ in range(N)]
    dp[0][0] = 1

    for k in range(1, M + 1):
        for i in range(N):
            dp[i][k] = dp[(i + 1) % N][k - 1] + dp[(i - 1) % N][k - 1]

    return dp[0][M]


if __name__ == '__main__':
    N, M = map(int, input().split())
    print(solve(N, M))
    # for i in range(3, 31):
    #     for j in range(1, 31):
    #         print(solve(i, j))
