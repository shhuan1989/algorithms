# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/13 21:26

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        if N == 1 and graph[0] == []:
            return 0

        target = (1 << N) - 1

        def bfs(start):
            vis = {(start, 1 << start)}
            q = [(start, 1 << start)]

            steps = 1
            while q:
                nq = []
                for u, state in q:
                    for v in graph[u]:
                        nstate = state | (1 << v)
                        if nstate == target:
                            return steps

                        s = (v, nstate)
                        if s not in vis:
                            vis.add(s)
                            nq.append(s)
                q = nq
                steps += 1

            return steps

        d = min([len(g) for g in graph])
        ans = min([bfs(i) for i in range(N) if len(graph[i]) == d])

        return ans


s = Solution()
print(s.shortestPathLength([[1,2,3],[0],[0],[0]]))
print(s.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))