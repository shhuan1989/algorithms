# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/6 10:37

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
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)
        us = set(s)
        m = len(us) + 1
        dp = [0 for _ in range(m)]
        sus = list(sorted(us))
        vi = {v:i for i, v in enumerate(sus)}
        s = [vi[v] for v in s]

        for i in range(1, n+1):
            ndp = [float('inf') for _ in range(m)]
            for j in range(m):
                ndp[j] = dp[j] + cost[i-1]

            ndp[s[i-1]] = min(ndp[s[i-1]], min([dp[j] for j in range(m) if j != s[i-1]] or [float('inf')]))
            dp = ndp

        return min(dp)


if __name__ == '__main__':
    s = Solution()
    # print(s.minCost(s = "abaac", cost = [1,2,3,4,5]))
    # print(s.minCost(s = "abc", cost = [1,2,3]))
    # print(s.minCost(s = "aabaa", cost = [1,2,3,4,1]))
    print(s.minCost("aaaaaaaaaaaaaa", [1,3,6,5,4,5,4,4,2,8,3,10,6,6]))
