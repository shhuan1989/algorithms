# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        if threshold <= 0:
            return [True for _ in range(len(queries))]
        
        parent = [i for i in range(n+1)]
        
        def find(u):
            pu = parent[u]
            if pu == u:
                return u
            pu = find(pu)
            parent[u] = pu
            return pu
        
        def merge(u, v):
            pu, pv = find(u), find(v)
            parent[pu] = pv
        
        
        
        for d in range(threshold + 1, n+1):
            u = d
            while u <= n:
                merge(u, d)
                u += d
        
        
        return [find(u) == find(v) for u, v in queries]
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.areConnected(n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]))
    print(s.areConnected(n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3],[2,2]]))
    print(s.areConnected(n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4],[2,2]]))