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
created by shhuan at 2020/7/9 21:11

"""

from functools import lru_cache


if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [i for i in range(1, N+1)]


    @lru_cache(maxsize=None)
    def solve(l, r):
        if l > r:
            return 1, []
        if l == r:
            return A[l], [B[l]]

        maxscore = -1
        maxroot = -1
        maxlp = []
        maxrp = []
        for ri in range(l, r+1):
            left, leftpre = solve(l, ri-1)
            right, rightpre = solve(ri+1, r)
            v = A[ri] + left * right
            if v > maxscore:
                maxscore = v
                maxroot = ri
                maxlp = leftpre
                maxrp = rightpre

        return maxscore, [B[maxroot]] + maxlp + maxrp

    s, p = solve(0, N-1)
    print(s)
    print(' '.join(map(str, p)))