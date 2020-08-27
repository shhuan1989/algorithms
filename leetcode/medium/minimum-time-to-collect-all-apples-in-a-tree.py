# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/26

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        def dfs(u, p, cost):
            apple, tcost = 0, 0
            
            num = 0
            for v in g[u]:
                if v == p:
                    continue
                a, b = dfs(v, u, cost + 1)
                if a > 0:
                    num += 1
                    apple += a
                    tcost += b + 1
            if num > 1:
                tcost -= (num - 1) * cost
            if hasApple[u]:
                apple += 1
                if apple == 1:
                    tcost = cost
            return apple, tcost
        
        a, b = dfs(0, -1, 0)
        
        return b



if __name__ == '__main__':
    s = Solution()
    print(s.minTime(4, [[0,1],[1,2],[0,3]], [True,True,True,True]))
    print(s.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False]))
    print(s.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False]))