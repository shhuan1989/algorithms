# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



class Solution:
    def minJump(self, jump: List[int]) -> int:
        
        n = len(jump)
        
        bit = [n for _ in range(n)]
        
        def update(index, val):
            while index < n:
                bit[index] = min(bit[index], val)
                index |= index + 1
                
        def query(index):
            mv = n
            while index >= 0:
                mv = min(mv, bit[index])
                index = (index & (index + 1)) - 1
            
            return mv

        dp = [n for _ in range(n)]
        pre = [[] for _ in range(n)]
        
        for i in range(n):
            if i + jump[i] >= n:
                dp[i] = 1
                update(i, 1)
            else:
                pre[i + jump[i]].append(i)
            
        for i in range(n-1, -1, -1):
            v = min(dp[i], query(i-1) + 1)
            for p in pre[i]:
                dp[p] = min(dp[p], v + 1)
                update(p, dp[p])
            if v < dp[i]:
                dp[i] = v
                update(i, v)
            
        return dp[0]
        
    
    
s = Solution()
print(s.minJump([2, 5, 1, 1, 1, 1]))
print(s.minJump([3,7,6,1,4,3,7,8,1,2,8,5,9,8,3,2,7,5,1,1]))
print(s.minJump([4,6,10,8,3,5,3,5,7,8,6,10,3,7,3,10,7,10,10,9,1,4,7,4,8,6,9,8,8,2,7,2,4,5,4,3,3,2,2,2,3,4,4,1,1,5,6,8,1,2]))

t0 = time.time()
print(s.minJump([1] * 10**6))
print(time.time() - t0)