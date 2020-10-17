# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/10/13 20:11

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
    def numberOfArrays(self, s: str, k: int) -> int:

        MOD = 10 ** 9 + 7
        n = len(s)

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        nums = [int(x) for x in s]
        ones = [i for i in range(n) if nums[i] > 0]

        maxl = 0
        while 10**maxl <= k:
            maxl += 1


        # oi = 0
        for i in range(n):

            # while oi < len(ones) and ones[oi] <= i:
            #     oi += 1
            # oi -= 1

            oi = bisect.bisect_right(ones, i) - 1

            v = 0
            for j in range(oi, -1, -1):
                if i-ones[j] >= maxl:
                    break
                v = v + 10 ** (i - ones[j]) * nums[ones[j]]
                # print(v)
                if v > k:
                    break
                dp[i + 1] += dp[ones[j]]
                dp[i + 1] %= MOD
        # print(dp)
        return dp[n]

if __name__ == '__main__':
    sys.stdin = open('restore-the-array.in', 'r')
    s = Solution()
    x = input().strip()
    t0 = time.time()
    print(s.numberOfArrays(x, 1000000000))
    print(time.time() -  t0)