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
created by shhuan at 2019/12/22 11:39

"""

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        crow = [poured]
        for r in range(query_row):
            nrow = [0 for _ in range(len(crow)+1)]
            for i, v in enumerate(crow):
                u = max(v - 1, 0)
                nrow[i] += u / 2
                nrow[i+1] += u / 2
            crow = nrow

        return min(crow[query_glass], 1.0)


s = Solution()
print(s.champagneTower(1, 1, 1))
print(s.champagneTower(2, 1, 1))
print(s.champagneTower(0, 1, 0))