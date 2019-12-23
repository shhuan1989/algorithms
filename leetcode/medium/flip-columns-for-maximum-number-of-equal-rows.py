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
created by shhuan at 2019/12/22 20:20

"""


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        N, M = len(matrix), len(matrix[0])
        rows = [''.join(map(str, row)) for row in matrix]
        nrows = [''.join(map(str, [v ^ 1 for v in row])) for row in matrix]
        ans = len([row for row in matrix if all([row[c] == row[0] for c in range(M)])])
        vis = set()
        for r1 in range(N):
            if r1 in vis:
                continue

            count = 1
            vis.add(r1)
            row1, nrow1 = rows[r1], nrows[r1]
            for r2 in range(N):
                if r1 == r2 or r2 in vis:
                    continue
                row2, nrow2 = rows[r2], nrows[r2]
                if row1 == row2 or row1 == nrow2 or nrow1 == row2 or nrow1 == nrow2:
                    vis.add(r2)
                    count += 1
            ans = max(ans, count)

        return ans

s = Solution()
print(s.maxEqualRowsAfterFlips([[0,1],[1,1]]))
print(s.maxEqualRowsAfterFlips([[0,1],[1,0]]))
print(s.maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]]))

t0 = time.time()
A = [[1 if random.randint(0, 10) > 5 else 0 for _ in range(300)] for _ in range(300)]
print(s.maxEqualRowsAfterFlips(A))
print(time.time() - t0)