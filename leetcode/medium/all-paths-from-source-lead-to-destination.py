# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/18/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
        
        def hasCircle(u, vis):
            
            for v in g[u]:
                if v in vis:
                    return True
                
                if hasCircle(v, vis|{v}):
                    return True
                
            return False
        
        
        if hasCircle(source, {source}):
            return False
        
        
        def dfs(u):
            if u == destination:
                return not g[u]
            
            if not g[u]:
                return False
            
            return all([dfs(v) for v in g[u]])
        
        return dfs(source)
    
s = Solution()
print(s.leadsToDestination(5, [[0,1],[1,2],[2,3],[3,4]], 1, 3))
print(s.leadsToDestination(3, [[0,1],[0,2]], 0, 2))
print(s.leadsToDestination(n = 3, edges = [[0,1],[1,1],[1,2]], source = 0, destination = 2))
print(s.leadsToDestination(n = 2, edges = [[0,1],[1,1]], source = 0, destination = 1))
print(s.leadsToDestination(n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination=3))
print(s.leadsToDestination(n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3))