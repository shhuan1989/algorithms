# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/10/14 19:35

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


if __name__ == '__main__':

    t0 = time.time()
    dp = [[0 for _ in range(2700)] for _ in range(101)]
    for i in range(26):
        dp[1][i] = 1

    MOD = 10**9+7
    for i in range(2, 101):
        dp[i][0] = 1
        for j in range(1, 2700):
            for k in range(26):
                if j-k >= 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % MOD

    print(time.time() - t0)
    T = int(input())
    for ti in range(T):
        s = input().strip()
        sm = sum([ord(v)-ord('a') for v in s])
        print(len(s), sm, dp[len(s)][sm]-1)
