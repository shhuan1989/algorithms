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
created by shhuan at 2019/12/18 21:53

"""

class UnionSet:
    def __init__(self):
        self.klen = collections.defaultdict(int)
        self.root = {}

    def uinon(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return -1

        kpu, kpv = max(self.klen[pu], 1), max(self.klen[pv], 1)

        if kpu < kpv:
            self.root[pu] = pv
            self.klen[pv] = kpu + kpv
        else:
            self.root[pv] = pu
            self.klen[pu] = kpu + kpv

        return kpu + kpv

    def find(self, u):
        if u not in self.root:
            return u
        parent = self.root[u]
        if parent < 0 or parent == u:
            return u

        ru = self.find(parent)
        self.root[u] = ru
        return ru

    def same(self, u, v):
        return self.find(u) == self.find(v)


class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        logs.sort()
        us = UnionSet()
        for t, a, b in logs:
            c = us.uinon(a, b)
            if c == N:
                return t

        return -1

s = Solution()
print(s.earliestAcq(logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], N = 6))
