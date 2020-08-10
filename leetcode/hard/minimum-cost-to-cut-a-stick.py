# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/9 11:02

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


from functools import lru_cache

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        @lru_cache(maxsize=None)
        def dfs(l, r):
            if r - l <= 1:
                return 0
            ans = math.inf
            for k in range(l+1, r):
                ans = min(ans, dfs(l, k) + dfs(k, r) + cuts[r]-cuts[l])

            return ans if ans != math.inf else 0

        cuts = [0] + cuts + [n]
        cuts.sort()
        return dfs(0, len(cuts)-1)


if __name__ == '__main__':
    s = Solution()
    print(s.minCost(7, [1, 3, 4, 5]))
    print(s.minCost(9, [5, 6, 1, 4, 2]))
    print(s.minCost(30, [18,15,13,7,5,26,25,29]))
    print(s.minCost(68, [15,19,12,43,63,35,33,21,58,37,11,5,45]))
    print(s.minCost(30, [13,25,16,20,26,5,27,8,23,14,6,15,21,24,29,1,19,9,3]))
    print(s.minCost(62, [6,61,45,49,27,47,10,17,24,39,32,54,59,48,26,30]))
    print(s.minCost(100, [78,83,75,77,93,68,64,21,8,80,46]))
    print(s.minCost(36, [13,17,15,18,3,22,27,6,35,7,11,28,26,20,4,5,21,10,8]))