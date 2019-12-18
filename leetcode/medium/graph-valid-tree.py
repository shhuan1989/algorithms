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
created by shhuan at 2019/12/18 22:33

"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)


        conn = [False] * n

        def dfs(u, p, vis):
            conn[u] = True
            for v in g[u]:
                if v != p:
                    if v in vis:
                        return False
                    if not dfs(v, u, vis | {v}):
                        return False

            return True

        if not dfs(0, -1, {0}):
            return False

        return all(conn)

s = Solution()
print(s.validTree( n = 5, edges = [[0,1], [0,2], [0,3], [1,4]]))
print(s.validTree( n = 5, edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]))
