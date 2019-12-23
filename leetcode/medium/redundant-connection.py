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
created by shhuan at 2019/12/19 23:15

"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ei = {}
        g = collections.defaultdict(list)
        for i, (u, v) in enumerate(edges):
            g[u].append(v)
            g[v].append(u)
            ei[(u, v)] = i
            ei[(v, u)] = i

        def dfs(u, p, path, vis):
            for v in g[u]:
                if v == p:
                    continue
                if v in vis:
                    i = path.index(v)
                    return path[i:]
                t = dfs(v, u, path+[v], vis | {v})
                if t:
                    return t

            return []

        path = dfs(1, -1, [1], {1})
        maxi = -1
        for i in range(len(path)):
            k = (path[i], path[(i+1) % len(path)])
            if ei[k] > maxi:
                maxi = ei[k]

        return edges[maxi]


s = Solution()
print(s.findRedundantConnection( [[1,2], [1,3], [2,3]]))
print(s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))