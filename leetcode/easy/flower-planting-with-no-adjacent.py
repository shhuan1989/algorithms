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
created by shhuan at 2019/12/11 23:59

"""

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        for u, v in paths:
            g[u].append(v)
            g[v].append(u)

        ans = [0 for _ in range(N+1)]

        def dfs(u):
            if ans[u] > 0:
                return

            used = {ans[v] for v in g[u]}
            for c in range(1, 5):
                if c not in used:
                    ans[u] = c
                    break
            for v in g[u]:
                dfs(v)

        for i in range(1, N+1):
            dfs(i)
        return ans[1:]

s = Solution()
print(s.gardenNoAdj(N = 3, paths = [[1,2],[2,3],[3,1]]))
print(s.gardenNoAdj(N = 4, paths = [[1,2],[3,4]]))
print(s.gardenNoAdj(N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]))