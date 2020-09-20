# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/16 10:56

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

from  functools import lru_cache
class Solution:
    def minDays(self, n: int) -> int:


        @lru_cache(maxsize=None)
        def dfs(n):
            if n <= 0:
                return 0

            if n > 100:
                a = float('inf')
                if n % 3 == 0:
                    a = min(a, 1 + dfs(n // 3))
                if n % 2 == 0:
                    a = min(a, 1 + dfs(n // 2))

                if (n - 1) % 3 == 0:
                    a = min(a, 2 + dfs((n-1) // 3))

                if (n-1) % 2 == 0:
                    a = min(a, 2 + dfs((n-1) // 2))

                if (n-2) % 3 == 0:
                    a = min(a, 3 + dfs((n-2) // 3))

                return a
            else:
                a = 1 + dfs(n-1)
                if n % 2 == 0:
                    a = min(a, 1 + dfs(n // 2))
                if n % 3 == 0:
                    a = min(a, 1 + dfs(n // 3))

                return a

        return dfs(n)


if __name__ == '__main__':
    s = Solution()
    # print(s.minDays(10))
    # print(s.minDays(6))
    # print(s.minDays(1))
    # print(s.minDays(56))
    # print(s.minDays(10**9))
    # print(s.minDays(182))
    # print(s.minDays(280))
    print(s.minDays(429))