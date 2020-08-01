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
created by shhuan at 2020/7/20 20:23

"""


if __name__ == '__main__':
    A, B, C = map(int, input().strip().split())

    def check(x):
        try:
            return B * sum([1.0 / ((1 + x) ** i) for i in range(1, C + 1)] or [0]) - A
        except:
            return 0

    def solve():
        lo, hi = 0, 10
        while abs(hi - lo) > 1e-9:
            d = (hi - lo) / 3
            l, r = lo + d, lo + 2 * d
            a, b, c = check(lo), check(l), check(r)
            if b * c < 0:
                lo, hi = l, r
            elif a * c > 0:
                lo = r
            else:
                hi = l

        print('{:.1f}'.format(lo * 100))

    solve()