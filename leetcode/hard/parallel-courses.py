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
created by shhuan at 2019/12/15 21:49

"""

class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:

        g = collections.defaultdict(list)
        d = collections.defaultdict(int)
        for u, v in relations:
            g[u].append(v)
            d[v] += 1

        ans = 0
        vis = [False for _ in range(N+1)]
        q = [i for i in range(1, N+1) if d[i] == 0]
        while q:
            nq = []
            ans += 1
            for u in q:
                vis[u] = True
                for v in g[u]:
                    d[v] -= 1
                    if d[v] == 0:
                        nq.append(v)
            q = nq
        if all([vis[i] for i in range(1, N+1)]):
            return ans

        return -1

s = Solution()
print(s.minimumSemesters(3, [[1, 3], [2, 3]]))
print(s.minimumSemesters(3, [[1, 2], [2, 3], [3, 1]]))


