# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2019/11/10 10:38

"""

from typing import List

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        A = [[0 for _ in range(m)] for _ in range(n)]
        for r, c in indices:
            for i in range(m):
                A[r][i] += 1
            for i in range(n):
                A[i][c] += 1

        ans = 0
        for r in range(n):
            for c in range(m):
                if A[r][c] % 2 == 1:
                    ans += 1
        return ans

s = Solution()
print(s.oddCells(n = 2, m = 3, indices = [[0,1],[1,1]]))
print(s.oddCells(n = 2, m = 2, indices = [[1,1],[0,0]]))

