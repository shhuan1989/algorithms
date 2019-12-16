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
created by shhuan at 2019/12/16 22:43

"""

class UnionSet:
    def __init__(self):
        self.klen = collections.defaultdict(int)
        self.root = {}

    def uinon(self, u, v):
        pu, pv = self.find(u), self.find(v)
        kpu, kpv = max(self.klen[pu], 1), max(self.klen[pv], 1)

        if kpu < kpv:
            self.root[pu] = pv
            self.klen[pv] = kpu + kpv
        else:
            self.root[pv] = pu
            self.klen[pu] += kpu + kpv

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
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        edges = [(w, u, v) for u, v, w in pipes] + [(w, 0, i+1) for i, w in enumerate(wells)]

        edges.sort()

        ans = 0
        us = UnionSet()
        for w, u, v in edges:
            if us.same(u, v):
                continue
            ans += w
            us.uinon(u, v)

        return ans


s = Solution()
print(s.minCostToSupplyWater(n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]))
print(s.minCostToSupplyWater(5, [46012,72474,64965,751,33304], [[2,1,6719],[3,2,75312],[5,3,44918]]))