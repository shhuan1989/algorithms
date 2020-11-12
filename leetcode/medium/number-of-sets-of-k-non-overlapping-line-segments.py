# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/10/19 20:03

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


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9+7
        dp = [[0 for _ in range(k + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
            dp[i][1] = i

        for j in range(2, k + 1):
            s = dp[0][j-1]
            t = 0
            for i in range(2, n):
                t += s + dp[i-1][j - 1]
                dp[i][j] = t % MOD
                s += dp[i-1][j-1]
                s %= MOD
                # dp[i][j] %= MOD

            # for i in range(2, n):
            #     for pi in range(i - 1, -1, -1):
            #         dp[i][j] += (i-pi) * dp[pi][j - 1]
            #         dp[i][j] %= MOD

        # for i in range(n):
        #     print(dp[i])
        return sum(dp[i][k] for i in range(n)) % MOD


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSets(4, 2))
    print(s.numberOfSets(3, 1))
    print(s.numberOfSets(30, 7))
    print(s.numberOfSets(5, 3))
    print(s.numberOfSets(3, 2))
    print(s.numberOfSets(1000, 800))