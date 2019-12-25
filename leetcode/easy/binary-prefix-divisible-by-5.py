# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/24/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = []
        s = 0
        for v in A:
            s *= 2
            s += v
            ans.append(s % 5 == 0)
        
        return ans
    
    
s = Solution()
print(s.prefixesDivBy5([0, 1, 1]))
print(s.prefixesDivBy5([1, 1, 1]))
print(s.prefixesDivBy5([0,1,1,1,1,1]))