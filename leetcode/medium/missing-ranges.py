# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/18/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            if lower < upper:
                return ['{}->{}'.format(lower, upper)]
            elif lower == upper:
                return [str(lower)]
            else:
                return []
        
        N = len(nums)
        ans = []
        
        if nums[0] > lower:
            l,  r = lower, min(upper, nums[0]-1)
            if l < r:
                ans.append('{}->{}'.format(l, r))
            else:
                ans.append(str(l))
        
        for i in range(N-1):
            if nums[i] < nums[i+1] - 1:
                l, r = nums[i]+1, nums[i+1]-1
                
                if l > upper:
                    break
                if r < lower:
                    continue
                l = max(l, lower)
                r = min(r, upper)
                
                if l == r:
                    ans.append(str(l))
                else:
                    ans.append('{}->{}'.format(l, r))
        if nums[-1] < upper:
            l, r = max(lower, nums[-1]+1), upper
            if l < upper:
                ans.append('{}->{}'.format(l, r))
            else:
                ans.append(str(l))
                    
        return ans

s = Solution()
# print(s.findMissingRanges([0, 1, 3, 50, 75], lower = 0, upper = 99))
print(s.findMissingRanges([0, 1, 3, 50, 75], lower = -2, upper = 2))