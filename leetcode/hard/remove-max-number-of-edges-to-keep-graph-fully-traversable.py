# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/6 10:55

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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n+1)]

        def find(u):
            pu = parent[u]
            if pu == u:
                return pu

            parent[u] = find(pu)
            return parent[u]

        def merge(u, v):
            pu, pv = find(u), find(v)
            parent[pu] = pv

        t1 = [(u, v) for t, u, v in edges if t == 1]
        t2 = [(u, v) for t, u, v in edges if t == 2]
        t3 = [(u, v) for t, u, v in edges if t == 3]

        ans = 0
        added = 0
        for u, v in t3:
            if find(u) != find(v):
                merge(u, v)
                added += 1
            else:
                ans += 1
        pb = parent.copy()
        ab = added
        for u, v in t1:
            if find(u) != find(v):
                merge(u, v)
                added += 1
            else:
                ans += 1

        if added < n-1:
            return -1

        parent = pb.copy()
        added = ab
        for u, v in t2:
            if find(u) != find(v):
                merge(u, v)
                added += 1
            else:
                ans += 1

        if added < n-1:
            return -1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
    print(s.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]))
    print(s.maxNumEdgesToRemove(n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]))
    print(s.maxNumEdgesToRemove(13, [[1,1,2],[2,2,3],[2,3,4],[1,3,5],[3,2,6],[2,3,7],[3,7,8],[3,2,9],[2,4,10],[2,9,11],[1,2,12],[3,4,13],[2,2,7],[1,1,9],[1,2,13],[2,7,13],[3,2,3],[1,7,10],[2,8,11],[1,2,7],[2,1,9],[2,2,9],[1,5,6],[2,4,9],[1,7,8],[1,4,6],[1,4,9],[3,7,13],[2,2,8],[2,2,6],[1,1,10],[1,1,11],[2,5,10],[1,2,9],[2,1,2],[1,3,4],[3,6,8],[3,6,13],[1,3,8],[1,1,6],[3,3,9],[1,2,3],[1,11,13]]))












