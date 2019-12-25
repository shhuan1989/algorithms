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
    def maxNumberOfApples(self, A: List[int]) -> int:
        A.sort()
        s = 0
        for i, v in enumerate(A):
            s += v
            if s > 5000:
                return i
        
        return len(A)

s = Solution()
print(s.maxNumberOfApples([100,200,150,1000]))
print(s.maxNumberOfApples([900,950,800,1000,700,800]))