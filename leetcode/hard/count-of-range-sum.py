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
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        
        n = len(nums)
        bit = [0 for _ in range(n + 1)]
        
        s = 0
        a = []
        for v in nums:
            s += v
            a.append(s)
        a.sort()
        
        def query(index):
            c = 0
            while index >= 0:
                c += bit[index]
                index = (index & (index + 1)) - 1
            return c
        
        def update(index):
            while index < n:
                bit[index] += 1
                index |= index + 1
                
        ans = 0
        s = 0
        for i, v in enumerate(nums):
            s += v
            
            # lower <= s-ps <= upper
            # s-upper <= ps <= s - lower
            
            # count of ps <= s-lower
            ca = query(bisect.bisect_right(a, s - lower) - 1)
            
            # count of ps < s-upper
            cb = query(bisect.bisect_left(a, s - upper) - 1)
            
            c = ca - cb
            ans += max(c, 0)
            if lower <= s <= upper:
                ans += 1
            update(bisect.bisect_left(a, s))

        return ans
        
        
s = Solution()
print(s.countRangeSum([0, -3, -3, 1, 1, 2], 3, 5))
print(s.countRangeSum([-2, 5, -1], -2, 2))
print(s.countRangeSum([2147483647, -2147483648, -1, 0], -1, 0))