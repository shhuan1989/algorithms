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
created by shhuan at 2020/7/11 16:18

"""


def solve(M, S, T):
    flash = min(M // 10, T)
    if flash * 60 >= S:
        return True, S // 60 if S % 10 == 0 else S // 60 + 1

    cost = flash
    dist = flash * 60
    S -= flash * 60
    T -= flash

    dp = [[float('-inf') for _ in range(14)] for _ in range(T+1)]
    M %= 10
    dp[0][M] = 0
    for t in range(T):
        for m in range(14):
            if m >= 10:
                dp[t+1][m-10] = max(dp[t+1][m-10], dp[t][m]+60)
            else:
                dp[t+1][m+4] = max(dp[t+1][m+4], dp[t][m])
                dp[t+1][m] = max(dp[t+1][m], dp[t][m] + 17)
            if dp[t][m] >= S:
                return True, cost + t

    d = max(dp[T])
    dist += 0 if d < 0 else d
    if d >= S:
        return True, cost + T
    return False, dist


if __name__ == '__main__':
    M, S, T = map(int, input().split())

    a, b = solve(M, S, T)
    if a:
        print('Yes')
        print(b)
    else:
        print('No')
        print(b)
