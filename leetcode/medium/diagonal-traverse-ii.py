# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/26

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        vals = collections.defaultdict(list)
        
        for r in range(len(nums)):
            row = nums[r]
            for c in range(len(row)):
                vals[r+c].append(nums[r][c])
        
        ans = []
        for r in sorted(vals.keys()):
            ans.extend(vals[r][::-1])
        
        return ans
    
    
s = Solution()
print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))
print(s.findDiagonalOrder([[1,2,3],[4],[5,6,7],[8],[9,10,11]]))
print(s.findDiagonalOrder([[1,2,3,4,5,6]]))