# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/13/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def __init__(self):
        self.index = 1
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        self.index = 1
        self.stack = []
        g = collections.defaultdict(list)
        
        for u, v in  connections:
            g[u].append(v)
            g[v].append(u)
        
        DFN, LOW, vis = [0] * (n+1), [0] * (n+1), [False] * (n+1)
        ret = []
        
        def tarjan(u, parent):
            DFN[u] = LOW[u] = self.index
            vis[u] = True
            self.index += 1
            self.stack.append(u)
            
            for v in g[u]:
                if v == parent:
                    continue
                if not vis[v]:
                    tarjan(v, u)
                    LOW[u] = min(LOW[u], LOW[v])
                    if LOW[v] > DFN[u]:
                        ret.append((u, v))
                else:
                    LOW[u] = min(LOW[u], DFN[v])
        
        tarjan(0, -1)
        
        return ret
        

s = Solution()
print(s.criticalConnections(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]))
            
                
                
            
            
            