# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/29

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import math
from functools import lru_cache

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        
        n = len(points)

        # pt = [[float('-inf') for _ in range(m)] for _ in range(n)]
        #
        # for s in range(n):
        #     pt[s][0] = points[s][0] + points[s][1]
        #
        # for t in range(1, m):
        #     for s in range(n):
        #         if s + (1 << t) <= n:
        #             pt[s][t] = max(pt[s][t - 1], pt[s + (1 << (t - 1))][t - 1])
        #         else:
        #             break
        
        @lru_cache(maxsize=None)
        def pt(s, t):
            if t == 0:
                return sum(points[s])
            
            return max(pt(s, t-1), pt(s+(1 << (t-1)), t-1))
        
        @lru_cache(maxsize=None)
        def query(s, t):
            if s > t:
                return float('-inf')
            
            if s == t:
                return sum(points[s])
            
            i = 0
            while (1 << i) <= t - s + 1:
                i += 1
            i -= 1
            
            return max(pt(s, i), query(s + (1 << i), t))
        
        x = [v[0] for v in points]
        # print([sum(v) for v in points])
        ans = float('-inf')
        for s in range(n):
            t = bisect.bisect_right(x, x[s] + k) - 1
            if s < t < n:
                # print(s + 1, t, query(s+1, t))
                ans = max(ans, points[s][1] - points[s][0] + query(s + 1, t))
        
        return ans
    
    def findMaxValueOfEquation2(self, points: List[List[int]], k: int) -> int:
        # print(len(points))
        #
        # ans = 0
        # ai, aj = -1, -1
        # for i in range(len(points)):
        #     for j in range(i+1, len(points)):
        #         x, y = points[j]
        #         px, py = points[i]
        #         if x-px > k:
        #             break
        #         v = x-px+y+py
        #         if v > ans:
        #             ans = v
        #             ai, aj = i, j
        # print(ans, ai, aj, points[ai], points[aj])
        
        
        q = []
        ans = float('-inf')
        for x, y in points:
            # dx = x-q[-1][0]
            # dy = y-q[-1][1]
            # dy > dx
            while q:
                dx = x - q[-1][0]
                dy = y - q[-1][1]
                if dx <= k and dx < dy:
                    px, py = q.pop()
                    ans = max(ans, abs(px-x) + y + py)
                else:
                    break
            # if q and abs(q[-1][0]-x) <= k:
            #     ans = max(ans, abs(q[-1][0]-x) + q[-1][1] + y)
            
            i = bisect.bisect_right(q, (x-k, float('-inf')))
            if i < len(q):
                px, py = q[i]
                ans = max(ans, x-px+y+py)
            
            q.append((x, y))
        # print(q)
        
        # nq = len(q)
        # for i in range(nq):
        #     for j in range(i+1, nq):
        #         x, y = q[j]
        #         px, py = q[i]
        #         if x-px > k:
        #             break
        #         ans = max(ans, x-px+y+py)
        
        return ans

    
if __name__ == '__main__':
    s = Solution()
    print(s.findMaxValueOfEquation([[-20,-14],[-17,-14],[-11,-12],[-8,-12],[-7,-2],[6,-1],[8,4],[9,-7],[13,20]], 13))
    # print(s.findMaxValueOfEquation([[-17,13],[2,1],[8,-5],[18,-20]], 26))
    # print(s.findMaxValueOfEquation(points=[[0, 0], [3, 0], [9, 2]], k=3))
    # print(s.findMaxValueOfEquation(points = [[1,3],[2,0],[5,10],[6,-10]], k = 1))
    # print(s.findMaxValueOfEquation([[-5, -1], [-4, -1], [11, 11], [15, -9]], 3))
    # print(s.findMaxValueOfEquation([[1, 3], [2, 0], [5, 10], [6, -10]], k=1))
    # print(s.findMaxValueOfEquation([[-19, 9], [-15, -19], [-5, -8]], 10))
    # print(s.findMaxValueOfEquation([[-19, -12], [-5, -18], [2, -2], [10, 3], [11, -3], [13, 17]], 13))
