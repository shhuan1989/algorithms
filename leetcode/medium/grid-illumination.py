# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/20 20:08

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
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        cols = collections.defaultdict(int)
        rows = collections.defaultdict(int)
        hill_diagonals = collections.defaultdict(int)
        dale_diagonals = collections.defaultdict(int)

        lamp_set = set()
        for row, col in lamps:  # 初始化，统计横竖对角线上灯的个数。
            cols[col] += 1
            rows[row] += 1
            hill_diagonals[row - col] += 1
            dale_diagonals[row + col] += 1
            lamp_set.add((row, col))  # 将灯的数组转化为字典

        def state(row, col):
            return bool(cols[col] + rows[row] + hill_diagonals[row - col] + dale_diagonals[row + col])

        def turn_off(row, col):
            for i in [-1, 0, 1]:
                if 0 <= i + row < N:
                    for j in [-1, 0, 1]:
                        if 0 <= col + j < N:
                            if (i + row, j + col) in lamp_set:
                                lamp_set.remove((i + row, j + col))
                                cols[j + col] -= 1
                                rows[i + row] -= 1
                                hill_diagonals[row + i - j - col] -= 1
                                dale_diagonals[row + i + j + col] -= 1

        res = []
        for row, col in queries:
            res.append(int(state(row, col)))
            turn_off(row, col)

        return res


s = Solution()
# print(s.gridIllumination(N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]))
# print(s.gridIllumination(5, [[0,0],[0,4]], [[0,4],[0,1],[1,4]]))
# print(s.gridIllumination(5, [[0,0],[1,0]], [[1,1],[1,1]]))
print(s.gridIllumination(5, [[0,0],[0,1],[0,4]], [[0,0],[0,1],[0,2]]))