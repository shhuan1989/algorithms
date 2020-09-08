# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/31

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        a, b, c, d = -1, -1, 0, 0
        for i, v in enumerate(nums):
            if v == 0:
                a = -1
                b = -1
                c = 0
                d = i + 1
            elif v < 0:
                c += 1
                if a < 0:
                    a = i
                elif b < 0:
                    b = i
            if c % 2 == 0:
                ans = max(ans, i - d + 1)
            elif a >= 0:
                ans = max(ans, i - a)
        
        return ans
    
if __name__ == '__main__':
    s = Solution()
    print(s.getMaxLen([1,-2,-3,4]))
    print(s.getMaxLen([0,1,-2,-3,-4]))
    print(s.getMaxLen( [-1,-2,-3,0,1]))
    print(s.getMaxLen([-1,2]))
    print(s.getMaxLen([1,2,3,5,-6,4,0,10]))