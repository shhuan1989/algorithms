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
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = [v for v in nums if v <= target]
        nums.sort()
        ans = 0
        n = len(nums)
        l, r = 0, n-1
        MOD = 10**9+7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                # for i in range(l, r+1):
                #     ans += 2**(max(i-l-1, 0))
                ans += 2**(r-l)
                ans %= MOD
                l += 1
                

        return ans
    
    
s = Solution()
print(s.numSubseq(nums = [3,5,6,7], target = 9))
print(s.numSubseq(nums = [3,3,6,8], target = 10))
print(s.numSubseq(nums = [2,3,3,4,6,7], target = 12))
print(s.numSubseq(nums = [5,2,4,1,7,6,8], target = 16))