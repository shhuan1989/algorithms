# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/20/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vis = [False for _ in range(n)]
        
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        def dfs(u):
            vis[u] = True
            for v in g[u]:
                if not vis[v]:
                    dfs(v)
        
        ans = 0
        for i in range(n):
            if not vis[i]:
                ans += 1
                dfs(i)
        return ans
