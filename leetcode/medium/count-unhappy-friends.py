# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/13 10:34

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


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:

        close = {}
        for x in range(n):
            close[(x, x)] = 0
            for i, y in enumerate(preferences[x]):
                close[(x, y)] = -i


        def getclose(x, y):
            return close[(x, y)]

        # print(close)
        unhappy = [0 for _ in range(n)]
        for cx, cy in pairs:
            for cu, cv in pairs:
                if cx == cu and cy == cv:
                    continue
                for x, y, u, v in [(cx, cy, cu, cv), (cx, cy, cv, cu), (cy, cx, cu, cv), (cy, cx, cv, cu)]:
                    if getclose(x, u) > getclose(x, y) and getclose(u, x) > getclose(u, v):
                        unhappy[x] = 1
                        # print(x)

        # print(unhappy)
        return sum(unhappy)


if __name__ == '__main__':
    s = Solution()
    print(s.unhappyFriends(n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]))
    print(s.unhappyFriends(n = 2, preferences = [[1], [0]], pairs = [[1, 0]]))
    print(s.unhappyFriends(n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]))
    print(s.unhappyFriends(4, [[1,3,2],[2,3,0],[1,0,3],[1,0,2]], [[2,1],[3,0]]))