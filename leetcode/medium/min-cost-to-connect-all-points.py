# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/13 10:49

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        def getdist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


        for i in range(n):
            for j in range(i+1, n):
                edges.append((getdist(points[i], points[j]), i, j))

        edges.sort()

        parent = [i for i in range(n)]
        def find(u):
            pu = parent[u]
            if pu == u:
                return pu

            pu = find(pu)
            parent[u] = pu

            return pu


        def merge(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            parent[pu] = pv
            return True


        ans = 0
        for d, u, v in edges:
            if merge(u, v):
                ans += d

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
    print(s.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
    print(s.minCostConnectPoints([[0,0],[1,1],[1,0],[-1,1]]))
    print(s.minCostConnectPoints([[-1000000,-1000000],[1000000,1000000]]))
    print(s.minCostConnectPoints([[0, 0]]))

