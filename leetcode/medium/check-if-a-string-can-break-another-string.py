# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        sa = list(sorted(s1))
        sb = list(sorted(s2))
        
        return all([a >= b for a, b in zip(sa, sb)]) or all([a >= b for a, b in zip(sb, sa)])
        
        
        
s = Solution()
print(s.checkIfCanBreak('abc', 'axy'))
        
        