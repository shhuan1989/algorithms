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
    def kthFactor(self, n: int, k: int) -> int:
        
        fs = []
        for i in range(1, n+1):
            if n % i == 0:
                fs.append(i)
        
        if len(fs) < k:
            return -1
        
        return fs[k-1]
    
s = Solution()
print(s.kthFactor(12, 3))
print(s.kthFactor(1, 1))
print(s.kthFactor(4, 4))
print(s.kthFactor(7, 2))
print(s.kthFactor(1000, 3))
        