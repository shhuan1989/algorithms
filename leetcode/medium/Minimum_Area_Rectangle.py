# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/17 23:39

"""


class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        xy = collections.defaultdict(list)
        yx = collections.defaultdict(list)
        points = {(x, y) for (x, y) in points}
        for x, y in points:
            xy[x].append(y)
            yx[y].append(x)

        for x in {x for x, y in points}:
            xy[x].sort()
        for y in {y for x, y in points}:
            yx[y].sort()

        ans = float('inf')
        for x1, y1 in points:
            x2s = yx[y1]
            xsi = bisect.bisect_left(x2s, x1 + 1)
            for x2 in x2s[xsi:]:
                w = x2 - x1
                y3s = xy[x2]
                y3i = bisect.bisect_left(y3s, y1 + 1)
                for y3 in y3s[y3i:]:
                    if (x1, y3) in points:
                        ans = min(ans, abs((x2 - x1) * (y3 - y1)))

        return ans if ans < float('inf') else 0

s = Solution()
print(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))