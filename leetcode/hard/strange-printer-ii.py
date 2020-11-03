# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/11/2

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
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        n, m = len(targetGrid), len(targetGrid[0])
        
        xlefttop = {}
        ylefttop = {}
        xrightbottom = {}
        yrightbottom = {}
        colors = set()
        colorCount = collections.defaultdict(int)
        
        for r in range(n):
            for c in range(m):
                color = targetGrid[r][c]
                colorCount[color] += 1
                xlefttop[color] = min(xlefttop.get(color, n), r)
                ylefttop[color] = min(ylefttop.get(color, m), c)
                xrightbottom[color] = max(xrightbottom.get(color, 0), r)
                yrightbottom[color] = max(yrightbottom.get(color, 0), c)
                colors.add(color)
        
        g = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for color in colors:
            x0, y0, x1, y1 = xlefttop[color], ylefttop[color], xrightbottom[color], yrightbottom[color]
            if colorCount[color] == (x1-x0+1) * (y1-y0+1):
                continue
            for r in range(x0, x1+1):
                for c in range(y0, y1+1):
                    if targetGrid[r][c] != color:
                        g[color].append(targetGrid[r][c])
                        indegree[targetGrid[r][c]] += 1
        
        q = collections.deque([c for c in colors if indegree[c] == 0])
        ans = []
        while q:
            u = q.popleft()
            ans.append(u)
            for v in g[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        # print(ans)
        return len(ans) == len(colors)
                    

if __name__ == '__main__':
    s = Solution()
    print(s.isPrintable( [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]))
    print(s.isPrintable([[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]))
    print(s.isPrintable([[1,2,1],[2,1,2],[1,2,1]]))
    print(s.isPrintable([[1,1,1],[3,1,3]]))