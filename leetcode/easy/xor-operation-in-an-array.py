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
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= start + 2 * i
        
        return ans
    
    
s = Solution()
print(s.xorOperation(5, 0))
print(s.xorOperation(4, 3))
print(s.xorOperation(1, 7))
print(s.xorOperation(10, 5))
