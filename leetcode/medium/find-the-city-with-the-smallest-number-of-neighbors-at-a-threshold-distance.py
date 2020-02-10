# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/26/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        dist = [[float('inf') for _ in range(n)] for _ in range(n)]
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
            dist[u][v] = w
            dist[v][u] = w
            
        for k in range(n):
            for u in range(n):
                for v in range(n):
                    if u != v:
                        dist[u][v] = min(dist[u][v], dist[u][k] + dist[v][k])
        
        # for row in dist:
        #     print(row)
        
        count = [0 for _ in range(n)]
        for u in range(n):
            for v in range(n):
                if dist[u][v] <= distanceThreshold:
                    count[u] += 1
        
        ans = -1
        mincount = float('inf')
        for city in range(n-1, -1, -1):
            if count[city] < mincount:
                mincount = count[city]
                ans = city
        # print(count)
        return ans
    
s = Solution()
print(s.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))
print(s.findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2))

        
                    