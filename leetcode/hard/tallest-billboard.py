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
created by shhuan at 2019/12/2 22:55

"""


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for i in rods:
            for k, b in list(dp.items()):
                dp[k + i] = max(dp.get(k + i, 0), b + i)
                dp[k - i] = max(dp.get(k - i, 0), b)
        return dp[0]


if __name__ == '__main__':
    s = Solution()
    print(s.tallestBillboard([1, 2, 3, 6]))
    print(s.tallestBillboard([1, 2, 3, 4, 5, 6]))
    print(s.tallestBillboard([1, 2]))
    t0 = time.time()
    print(s.tallestBillboard([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 50, 50, 50, 150, 150, 150, 100, 100, 100, 123]))
    print(time.time() - t0)
