# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/29

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        bit = [0 for _ in range(n)]
        a = list(sorted(nums))
        
        def update(index):
            while index < n:
                bit[index] += 1
                index |= index + 1
        
        def query(index):
            c = 0
            while index >= 0:
                c += bit[index]
                index = (index & (index + 1)) - 1
            
            return c
        
        ans = []
        for i in range(n-1, -1, -1):
            v = nums[i]
            ans.append(query(bisect.bisect_left(a, v) - 1))
            update(bisect.bisect_left(a, v))
        
        return ans[::-1]
        
        
s = Solution()
print(s.countSmaller([5,2,6,1]))
print(s.countSmaller([-1,-1]))