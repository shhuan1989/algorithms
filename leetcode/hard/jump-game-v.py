# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/2/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        g = collections.defaultdict(list)
        A = arr
        N = len(A)
        for i in range(N):
            for j in range(i+1, min(N, i+d+1)):
                if A[i] <= A[j]:
                    break
                g[i].append(j)
            
            for j in range(i-1, max(-1, i-d-1), -1):
                if A[i] <= A[j]:
                    break
                    
                g[i].append(j)
        
        
        # print(g)
        
        ans = [1 for _  in range(N)]
        
        def dfs(node, parent):
            if ans[node] > 1:
                return ans[node]
            
            dist = 1
            for v in g[node]:
                if v != parent:
                    dist = max(dist, 1 + dfs(v, node))
            
            ans[node] = dist
            return dist
        
        for i in range(N):
            dfs(i, -1)
        return max(ans)
    
s = Solution()
print(s.maxJumps([6,4,14,6,8,13,9,7,10,6,12], d = 2))
print(s.maxJumps(arr = [3,3,3,3,3], d = 3))
print(s.maxJumps(arr = [7,6,5,4,3,2,1], d = 1))
print(s.maxJumps(arr = [7,1,7,1,7,1], d = 2))
print(s.maxJumps(arr = [66], d = 1))


import random
print(s.maxJumps([random.randint(0, 1000)], 1000))
                
        
        