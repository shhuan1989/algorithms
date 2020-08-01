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
created by shhuan at 2020/7/25 12:00

"""


if __name__ == '__main__':
    N, K = map(int, input().split())

    dp = [0 for _ in range(N+1)]
    dp[0] = 1

    MOD = 100003
    for i in range(1, N+1):
        for j in range(max(0, i-K), i):
            dp[i] += dp[j]
            dp[i] %= MOD

    print(dp[N])