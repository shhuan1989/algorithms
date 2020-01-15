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
created by shhuan at 2020/1/14 22:22

"""


def solve(N, M, A):
    def check(ops):
        pv = 0
        for v in A:
            if v-ops >= 0 and v+ops < M:
                if v + ops < pv:
                    return False
                pv = max(pv, v-ops)
            elif v - ops >= 0 and v + ops >= M:
                l = (v + ops) % M
                if l >= pv:
                    pass
                else:
                    l, r = v-ops, M-1
                    pv = max(pv, l)
            elif v - ops < 0 and v + ops < M:
                if v + ops >= pv:
                    pass
                else:
                    l = (v-ops) % M
                    pv = max(pv, l)
            else:
                pass

        return True

    lo, hi = 0, max(N, M)
    while lo <= hi:
        m = (lo + hi) // 2
        if check(m):
            hi = m - 1
        else:
            lo = m + 1
    return lo



N, M = map(int, input().split())
A = [int(x) for x in input().split()]
print(solve(N, M, A))