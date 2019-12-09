# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/6/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a, b = 0, 0
        
        N, M = len(arr1), len(arr2)
        for i, v in enumerate(arr1):
            a += (1 if (N-i-1) % 2 == 0 else -1) * v * (1 << (N-i-1))
        
        for i, v in enumerate(arr2):
            b += (1 if (M-i-1) % 2 == 0 else -1) * v * (1 << (M-i-1))
            
        c = a + b
        ans = []
        while c != 0:
            if c % 2 == 0:
                ans.append(0)
                c //= -2
            else:
                ans.append(1)
                c = (c-1) // (-2)
        
        return ans[::-1] if ans else [0]
        
        
    
        
s = Solution()
# print(s.addNegabinary(arr1 = [1,1,1,1,1], arr2 = [1,0,1]))
print(s.addNegabinary([0], [1, 1]))