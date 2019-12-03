# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/2/19

"""

import collections
import time
import os
import sys
import bisect
import heapq

from typing import List
import math

class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        
        def dfs(a, p):
            if not a:
                return 1
            
            ans = 0
            vs = set()
            for i, v in enumerate(a):
                if v in vs:
                    continue
                u = int(math.sqrt(v+p))
                if u * u == (v+p):
                    vs.add(v)
                    ans += dfs(a[:i] + a[i+1:], v)
            
            return ans
        
        wc = {v: i for i, v in enumerate(A)}
        return sum([dfs(A[:i] + A[i+1:], A[i]) for i in wc.values()])
    
s = Solution()
print(s.numSquarefulPerms([1, 17, 8]))
print(s.numSquarefulPerms([2, 2, 2]))
