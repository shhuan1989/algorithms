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
created by shhuan at 2019/12/17 23:06

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
            self.klen[pu] = kpu + kpv

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
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        def neighbors(x, y):
            return [(nx, ny) for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] if 0 <= nx < m and 0 <= ny < n]

        id = 1
        group = {}
        count = 0
        ans = []
        us = UnionSet()
        marked = set()
        for r, c in positions:
            if (r, c) in marked:
                ans.append(count)
                continue
            marked.add((r, c))
            neighborIslands = []
            for nr, nc in neighbors(r, c):
                if (nr, nc) in group:
                    neighborIslands.append(group[(nr, nc)])

            if not neighborIslands:
                id += 1
                group[(r, c)] = id
                count += 1
            else:
                neighborIslands = {us.find(u) for u in neighborIslands}
                count -= len(neighborIslands) - 1
                neighborIslands = list(neighborIslands)
                for u in neighborIslands[1:]:
                    us.uinon(neighborIslands[0], u)
                group[(r, c)] = neighborIslands[0]

            ans.append(count)
        return ans

s = Solution()
print(s.numIslands2( m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]))
print(s.numIslands2(3, 3, [[0,0],[0,1],[1,2],[1,2]]))



