# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/22 12:24

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
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        team = collections.defaultdict(list)
        for v, g in enumerate(group):
            team[g].append(v)

        beforeItems = [set(x) for x in beforeItems]

        def topo(items):
            items = set(items)
            g = collections.defaultdict(list)
            d = collections.defaultdict(int)
            for v in items:
                d[v] = 0

            for v in items:
                for u in beforeItems[v]:
                    if u in items:
                        g[u].append(v)
                        d[v] += 1

            ans = []
            while d:
                vs = [v for v, c in d.items() if c == 0]
                if not vs:
                    break
                for v in vs:
                    ans.append(v)
                    del d[v]
                    for u in g[v]:
                        d[u] -= 1
            return ans if len(ans) == len(items) else []


        steam = collections.defaultdict(list)
        mk = max(team.keys()) + 10
        for k, v in team.items():
            if k != -1:
                steam[k] = topo(v)
                if len(steam[k]) != len(v):
                    return []
            else:
                for x in v:
                    steam[mk] = [x]
                    group[x] = mk
                    mk += 1

        groupdep = collections.defaultdict(set)
        for u in range(n):
            for v in beforeItems[u]:
                gu, gv = group[u], group[v]
                if gu != gv:
                    groupdep[gv].add(gu)




        def topog(items):
            g = collections.defaultdict(list)
            d = collections.defaultdict(int)
            for v in items:
                d[v] = 0

            for u in items:
                for v in groupdep[u]:
                    g[u].append(v)
                    d[v] += 1

            ans = []
            while d:
                vs = [v for v,c in d.items() if c == 0]
                if not vs:
                    break
                for v in vs:
                    ans.append(v)
                    del d[v]
                    for u in g[v]:
                        d[u] -= 1
            return ans

        y = [g for g in steam.keys()]
        x = topog(y)
        if len(x) != len(y):
            return []

        ans = []
        for g in x:
            ans += steam[g]

        index = {v:i for i, v in enumerate(ans)}
        for i, v in enumerate(ans):
            if any([index[u] >= i for u in beforeItems[v]]):
                return []

        return ans

s = Solution()
print(s.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]))
print(s.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]))
print(s.sortItems(8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3],[],[4],[]]))
print(s.sortItems(10, 4, [2, 2, 2, 1, 0, 1, 3, 2, 0, 1], [[7, 6, 2, 5, 3], [], [], [], [7], [], [], [], [], []]))