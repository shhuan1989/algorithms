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
created by shhuan at 2019/12/20 20:00

"""


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        ci = collections.defaultdict(list)
        for i, v in enumerate(colors):
            ci[v].append(i)

        INF = len(colors) + 1
        ans = []
        for i, c in queries:
            x = ci[c]
            if not x:
                ans.append(-1)
                continue
            l, r = bisect.bisect_left(x, i), bisect.bisect_right(x, i)
            d = INF
            if 0 <= l < len(x):
                d = min(d, abs(i-x[l]))
                if l > 0:
                    d = min(d, abs(i-x[l-1]))
            if 0 <= r < len(x):
                d = min(d, abs(i-x[r]))
            elif r == len(x):
                d = min(d, i - x[-1])
            ans.append(d if d < INF else -1)

        return ans

    def shortestDistanceColor2(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        N = len(colors)
        right = [[N for _ in range(4)] for _ in range(N+1)]

        for i in range(N-1, -1, -1):
            for c in range(4):
                right[i][c] = right[i+1][c]
            c = colors[i]
            right[i][c] = i

        left = [[-1 for _ in range(4)] for _ in range(N)]
        left[0][colors[0]] = 0
        for i in range(1, N):
            for c in range(4):
                left[i][c] = left[i-1][c]
            c = colors[i]
            left[i][c] = i

        ans = []
        for i, c in queries:
            l, r = left[i][c], right[i][c]
            d = N
            if l >= 0:
                d = i-l
            if r < N:
                d = min(d, r-i)
            ans.append(d if d < N else -1)

        return ans


s = Solution()
print(s.shortestDistanceColor([2,1,2,2,1], [[2,1]]))
print(s.shortestDistanceColor(colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]))
print(s.shortestDistanceColor(colors = [1,2], queries = [[0,3]]))
