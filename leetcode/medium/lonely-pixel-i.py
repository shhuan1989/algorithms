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
created by shhuan at 2019/12/19 20:45

"""

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows, cols = collections.defaultdict(list), collections.defaultdict(list)
        N, M = len(picture), len(picture[0])

        for r in range(N):
            for c in range(M):
                if picture[r][c] == 'B':
                    rows[r].append(c)
                    cols[c].append(r)

        ans = 0
        for r, cs in rows.items():
            if len(cs) == 1:
                if len(cols[cs[0]]) == 1:
                    ans += 1
        return ans
s = Solution()
print(s.findLonelyPixel([['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]))