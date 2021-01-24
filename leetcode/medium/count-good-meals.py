# -*- coding: utf-8 -*-

"""
created by shhuan at 2021/1/3 10:34

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
    def countPairs(self, deliciousness: List[int]) -> int:
        wc = collections.Counter(deliciousness)

        ans = 0
        MOD = 10**9+7
        for x, c in wc.items():
            for k in range(25):
                y = 2 ** k - x
                if x < y:
                    ans += c * wc[y]
                    ans %= MOD
                elif x == y:
                    ans += c * (c-1) // 2
                    ans %= MOD

        return ans % MOD


if __name__ == '__main__':
    s = Solution()
    print(s.countPairs([1, 3, 5, 7, 9]))
    print(s.countPairs([1,1,1,3,3,3,7]))