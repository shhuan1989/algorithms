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
created by shhuan at 2019/12/6 23:53

"""

class Solution(object):
    def catMouseGame(self, graph):
        N = len(graph)
        MOUSE, CAT, DRAW = 1, 2, 0

        def parents(u, v, t):
            if t == CAT:
                for w in graph[u]:
                    yield (w, v, MOUSE)
            else:
                for w in graph[v]:
                    if w != 0:
                        yield (u, w, CAT)

        color = collections.defaultdict(int)
        q = []
        for i in range(N):
            for t in [1, 2]:
                color[0, i, t] = MOUSE
                q.append((0, i, t, MOUSE))
                if i > 0:
                    color[i, i, t] = CAT
                    q.append((i, i, t, CAT))

        degree = collections.defaultdict(int)
        for m in range(N):
            for c in range(N):
                degree[m, c, MOUSE] = len(graph[m])
                degree[m, c, CAT] = len(graph[c]) - (1 if 0 in graph[c] else 0)

        q = collections.deque(q)
        while q:
            u, v, t, c = q.popleft()
            for u2, v2, t2 in parents(u, v, t):
                if color[u2, v2, t2] == DRAW:
                    if t2 == c:
                        color[u2, v2, t2] = c
                        q.append((u2, v2, t2, c))
                    else:
                        degree[u2, v2, t2] -= 1
                        if degree[u2, v2, t2] == 0:
                            color[u2, v2, t2] = 3 - t2
                            q.append((u2, v2, t2, 3-t2))
        return color[1, 2, 1]

s = Solution()
print(s.catMouseGame([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]))
print(s.catMouseGame([[1,3],[0],[3],[0,2]]))
print(s.catMouseGame([[6],[4],[9],[5],[1,5],[3,4,6],[0,5,10],[8,9,10],[7],[2,7],[6,7]]))