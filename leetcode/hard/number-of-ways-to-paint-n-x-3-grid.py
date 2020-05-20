# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/4/13

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def numOfWays(self, n: int) -> int:
        
        vs = []
        for a in range(3):
            for b in range(3):
                if a == b:
                    continue
                for c in range(3):
                    if b != c:
                        vs.append((a, b, c))
        
        def neb(a, b, c):
            return [i for i, v in enumerate(vs) if a != v[0] and b != v[1] and c != v[2]]
        
        dp = [1 for _ in range(len(vs))]
        
        pre = [neb(a, b, c) for (a, b, c) in vs]
        
        MOD = 10**9+7
        for i in range(1, n):
            dp = [sum([dp[k] for k in pre[j]]) % MOD for j in range(len(vs))]

        return sum(dp) % MOD

    
s = Solution()
print(s.numOfWays(1))
print(s.numOfWays(2))
print(s.numOfWays(3))
print(s.numOfWays(7))
print(s.numOfWays(5000))
print(s.numOfWays(2727))

