# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/8/25 23:41


类似于洗牌的算法,
把二维数组M*N变成一维的数组,[x_0, x_1, ... x_{MxN-1}],
随机选取一个,之后把他和最后一个没使用的位置交换,数组变成[未使用的位置]+[使用过的位置].
因为效率问题,把
a[i], a[last] = a[last], a[i]
last -= 1

变成
map[i], map[last] = map[last], map[i]
last -= 1
"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List
import random


class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.total = n_rows * n_cols
        self.d = {}
        self.r, self.c = n_rows, n_cols

    def flip(self) -> List[int]:
        i = random.randint(0, self.total - 1)
        self.total -= 1
        res = self.d.get(i, i)
        # exchange the numbers at index self.total and m
        self.d[i], self.d[self.total] = self.d.get(self.total, self.total), res
        return (res // self.c, res % self.c)

    def reset(self) -> None:
        self.total = self.r * self.c



s = Solution(2, 2)
s.used=[1,4]
s.count=2

s.flip()
s.flip()
s.reset()

