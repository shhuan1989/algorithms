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
created by shhuan at 2019/12/15 17:32

"""

class SegmentTree:
    def __init__(self, data):
        if not data:
            N, M = 0, 0
        else:
            N, M = len(data), len(data[0])
        self.N = N
        self.M = M
        self.data = data
        self.tree = [[0 for _ in range(4*M+1)] for _ in range(4*N+1)]
        if N > 0 and M > 0:
            self.build_x(1, 0, N-1)

    def build_x(self, vx, lx, rx):
        if lx != rx:
            mx = (lx + rx) // 2
            self.build_x(vx * 2, lx, mx)
            self.build_x(vx * 2 + 1, mx + 1, rx)

        self.build_y(vx, lx, rx, 1, 0, self.M-1)

    def build_y(self, vx, lx, rx, vy, ly, ry):
        if ly == ry:
            if lx == rx:
                self.tree[vx][vy] = self.data[lx][ly]
            else:
                self.tree[vx][vy] = self.tree[vx*2][vy] + self.tree[vx*2+1][vy]
        else:
            my = (ly + ry) // 2
            self.build_y(vx, lx, rx, vy*2, ly, my)
            self.build_y(vx, lx, rx, vy*2+1, my+1, ry)
            self.tree[vx][vy] = self.tree[vx][vy*2] + self.tree[vx][vy*2+1]

    def sum_y(self, vx, vy, nodely, nodery, targetly, targetry):
        if targetly > targetry:
            return 0
        if nodely == targetly and nodery == targetry:
            return self.tree[vx][vy]

        nodemy = (nodely + nodery) // 2
        return self.sum_y(vx, vy*2, nodely, nodemy, targetly, min(targetry, nodemy)) + \
               self.sum_y(vx, vy*2+1, nodemy+1, nodery, max(targetly, nodemy+1), targetry)

    def sum_x(self, vx, nodelx, noderx, targetlx, targetrx, targetly, targetry):
        if targetlx > targetrx:
            return 0

        if nodelx == targetlx and noderx == targetrx:
            return self.sum_y(vx, 1, 0, self.M-1, targetly, targetry)

        nodemx = (nodelx + noderx) // 2
        return self.sum_x(vx * 2, nodelx, nodemx, targetlx, min(nodemx, targetrx), targetly, targetry) + \
               self.sum_x(vx*2+1, nodemx+1, noderx, max(targetlx, nodemx+1), targetrx, targetly, targetry)

    def update_y(self, vx, vy, nodelx, noderx, nodely, nodery, x, y, newval):
        if nodely == nodery:
            if nodelx == noderx:
                self.tree[vx][vy] = newval
            else:
                self.tree[vx][vy] = self.tree[vx*2][vy] + self.tree[vx*2+1][vy]
        else:
            nodemy = (nodely + nodery) // 2
            if y <= nodemy:
                self.update_y(vx, vy*2, nodelx, noderx, nodely, nodemy, x, y, newval)
            else:
                self.update_y(vx, vy*2+1, nodelx, noderx, nodemy+1, nodery, x, y, newval)
            self.tree[vx][vy] = self.tree[vx][vy*2] + self.tree[vx][vy*2+1]

    def update_x(self, vx, nodelx, noderx, x, y, newval):
        if nodelx != noderx:
            nodemx = (nodelx + noderx) // 2
            if x <= nodemx:
                self.update_x(vx*2, nodelx, nodemx, x, y, newval)
            else:
                self.update_x(vx*2+1, nodemx+1, noderx, x, y, newval)
        self.update_y(vx, 1, nodelx, noderx, 0, self.M-1, x, y, newval)

    def update(self, x, y, newval):
        self.update_x(1, 0, self.N-1, x, y, newval)

    def sum(self, lx, rx, ly, ry):
        if rx >= self.N or ry >= self.M:
            return 0
        return self.sum_x(1, 0, self.N-1, lx, rx, ly, ry)


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.seg = SegmentTree(matrix)

    def update(self, row: int, col: int, val: int) -> None:
        self.seg.update(row, col, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.seg.sum(row1, row2, col1, col2)

# s = NumMatrix([
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ])
# print(s.sumRegion(2, 1, 4, 3))
# s.update(3, 2, 2, )
# print(s.sumRegion(2, 1, 4, 3))

s = NumMatrix([[]])
print(s.sumRegion(0, 0, 0, 0))