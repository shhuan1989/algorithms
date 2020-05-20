# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/10/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        us = [i for i in range(n)]
        size = [1 for i in range(n)]
        
        def find(u):
            if us[u] == u:
                return u
            
            pu = find(us[u])
            us[u] = pu
            
            return pu
        
        def merge(u, v):
            pu, pv = find(u), find(v)
            su, sv = size[pu], size[pv]
            if su < sv:
                us[pu] = pv
                size[pv] = su + sv
            else:
                us[pv] = pu
                size[pu] = su + sv
                
        for u, v in connections:
            merge(u, v)
            
        lines = collections.defaultdict(int)
        for u, v in connections:
            lines[find(u)] += 1
        
        groups = collections.defaultdict(int)
        for u in range(n):
            pu = find(u)
            groups[pu] += 1
        
        extralines = sum([lines[g] - s + 1 for g, s in groups.items()])
        
        if extralines >= len(groups) - 1:
            return len(groups) - 1
        
        return - 1


s = Solution()
print(s.makeConnected(4, [[0,1],[0,2],[1,2]]))
print(s.makeConnected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]))
print(s.makeConnected(6, [[0,1],[0,2],[0,3],[1,2]]))
print(s.makeConnected(5, [[0,1],[0,2],[3,4],[2,3]]))