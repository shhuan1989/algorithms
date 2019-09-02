# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/1 14:05


返回二维数组中， 边上数字全是1的子正方形的面积


记录每个位置往上下左右走最多有多少个1，
然后遍历每个点(r, c)，假设往右和下分别最多wright, hdown个1，那么正方形边长不会超过l=min(wright, hdown)；
然后对于每个可能的长度，右下角的点位置是(r',c')=(r+l-1, c+l-1)，然后看(r', c') 往上和左最多hup, wleft个1；
如果min(hup, wleft) >= l，就可以组成边长为l的正方形。

初始化需要O(N^2)，遍历时对每个点需要O(N)搜索，所以复杂度总共是O(N^3)

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
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        hup, wleft = [[0 for _ in range(n)] for _ in range(m)], [[0 for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    hup[r][c] = (hup[r-1][c] if r > 0 else 0) + 1
                    wleft[r][c] = (wleft[r][c-1] if c > 0 else 0) + 1

        hdown, wright = [[0 for _ in range(n)] for _ in range(m)], [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if grid[r][c] == 1:
                    hdown[r][c] = (hdown[r+1][c] if r+1 < m else 0) + 1
                    wright[r][c] = (wright[r][c+1] if c+1 < n else 0) + 1


        ans = 0
        for r in range(m):
            for c in range(n):
                l = min(wright[r][c], hdown[r][c])
                if l > ans:
                    for l in range(l, ans, -1):
                        right, bottom = r+l-1, c+l-1
                        if min(hup[right][bottom], wleft[right][bottom]) >= l:
                            ans = l
                            break
        return ans*ans




    # TLE
    def largest1BorderedSquare1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for l in range(max(m, n), 0, -1):
            for sr in range(m-l+1):
                for sc in range(n-l+1):
                    if all([grid[sr][c]==1 for c in range(sc, sc+l)]) and \
                        all([grid[sr+l-1][c] for c in range(sc, sc+l)]) and \
                        all([grid[r][sc] for r in range(sr, sr+l)]) and \
                        all([grid[r][sc+l-1] for r in range(sr, sr+l)]):
                        return l*l

        return 0


s = Solution()
print(s.largest1BorderedSquare(grid = [[1,1,1],[1,0,1],[1,1,1]]))
# print(s.largest1BorderedSquare(grid = [[1,1,0,0]]))
# print(s.largest1BorderedSquare([[0]]))
# print(s.largest1BorderedSquare([[1,1,1],[1,1,0],[1,1,1],[0,1,1],[1,1,1]]))
print(s.largest1BorderedSquare(
    [
        [0,1,0,1,1],
        [1,1,1,1,1],
        [1,1,0,1,1],
        [1,1,1,1,0],
        [0,1,1,1,1],
        [1,1,1,0,1],
        [0,1,1,1,1],
        [1,1,1,0,1]
    ]
))