# -*- coding: utf-8 -*-

"""
created by shhuan at 2021/1/24 17:06

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from functools import lru_cache
from typing import List

sys.setrecursionlimit(1000000)

from functools import lru_cache
from typing import List


class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        maxn = 10 ** 4 + 10

        # factors = [set() for _ in range(maxn)]
        # factors[2].add(2)
        # for x in range(3, maxn):
        #     for y in range(2, int(math.sqrt(x)) + 2):
        #         if x % y == 0:
        #             factors[x].add(y)
        #             factors[x].add(x // y)
        #     factors[x].add(x)

        @lru_cache(maxsize=None)
        def factors(x):
            if x == 2:
                return [2]
            if x < 2:
                return []

            ans = set()
            for y in range(2, int(math.sqrt(x)) + 2):
                if x % y == 0:
                    ans.add(x // y)
                    ans.add(y)

            return ans

        @lru_cache(maxsize=None)
        def dfs(x, y):
            if x == 1:
                return 0
            if y == 1:
                return 1

            return sum([dfs(x // v, y - 1) for v in factors(x)])

        fact = [1 for _ in range(maxn)]
        for i in range(2, maxn):
            fact[i] = i * fact[i - 1]
            fact[i] %= mod

        @lru_cache(maxsize=None)
        def inv(x):
            return pow(x, mod - 2, mod)

        @lru_cache(maxsize=None)
        def ncr(c, r):
            if r == 0 or r == c:
                return 1
            if r == 1:
                return c

            return (fact[c] * inv(fact[c - r] * fact[r])) % mod

        # @lru_cache(maxsize=None)
        # def ncr(c, r):
        #     if c == 0 or r == c:
        #         return 1
        #
        #     if r == 1:
        #         return c
        #
        #     return (ncr(c - 1, r - 1) + ncr(c - 1, r)) % mod

        @lru_cache(maxsize=None)
        def solve(x, y):
            if x == 1 or y == 1:
                return 1

            ans = 0
            for z in range(1, min(20, y + 1)):
                w = dfs(x, z)
                ans += w * ncr(y, z)
                ans %= mod
            return ans

        return [solve(x, y) for y, x in queries]


if __name__ == '__main__':
    s = Solution()
    print(s.waysToFillArray([[2, 6], [5, 1], [73, 660]]))
    print(s.waysToFillArray([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))
    