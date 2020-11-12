# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/29

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

from itertools import combinations


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        if not dependencies:
            return n // k if n % k == 0 else n // k + 1

        ds = set()
        to = collections.defaultdict(list)
        indegree = [0 for _ in range(n + 1)]
        for u, v in dependencies:
            to[u].append(v)
            indegree[v] += 1
            ds.add(u)
            ds.add(v)

        def dfs(curr, vis, ind):
            if not curr:
                return 0

            # print(curr, vis, ind)
            ans = 10000
            for x in combinations(curr, min(k, len(curr))):
                for y in x:
                    for z in to[y]:
                        ind[z] -= 1

                nc = {v for v in curr if v not in x}
                nvis = vis | set(x)
                nc |= {v for v in range(1, n + 1) if ind[v] == 0 and v not in nvis}
                ans = min(ans, 1 + dfs(list(nc), nvis, ind))

                for y in x:
                    for z in to[y]:
                        ind[z] += 1

            return ans

        pre = [v for v in range(1, n + 1) if v not in ds]
        if len(pre) > 2 * k:
            ans = len(pre) // k - 1
            vis = set(pre[:ans * k])
            ans += dfs([v for v in range(1, n + 1) if indegree[v] == 0 and v not in vis], vis, indegree)
            return ans
        else:
            return dfs([v for v in range(1, n + 1) if indegree[v] == 0], set(), indegree)


if __name__ == '__main__':
    s = Solution()
    print(s.minNumberOfSemesters(n=4, dependencies=[[2, 1], [3, 1], [1, 4]], k=2))
    print(s.minNumberOfSemesters(n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2))
    print(s.minNumberOfSemesters(n = 11, dependencies = [], k = 2))
    print(s.minNumberOfSemesters(15, [[2,1]], 4))
    print(s.minNumberOfSemesters(15, [[8, 9], [11, 1], [2, 9]], 14))