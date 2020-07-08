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


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ones = []
        s = -1
        for i, v in enumerate(nums):
            if v == 1:
                if s < 0:
                    s = i
            else:
                if s >= 0:
                    ones.append((s, i-1))
                    s = -1
        if s >= 0:
            ones.append((s, len(nums)-1))
        
        ans = max([b-a+1 for a, b in ones] or [0])
        
        for i in range(len(ones)-1):
            a, b = ones[i]
            c, d = ones[i+1]
            if c == b + 2:
                ans = max(ans, d-a)
        
        return min(ans, len(nums)-1)
    
    
s = Solution()
print(s.longestSubarray([1, 1, 0, 1]))
print(s.longestSubarray( [0,1,1,1,0,1,1,0,1]))
print(s.longestSubarray([1, 1, 1]))
print(s.longestSubarray([1,1,0,0,1,1,1,0,1]))
print(s.longestSubarray([0,0,0]))
