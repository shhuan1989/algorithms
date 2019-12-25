# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/23/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sh = list(sorted(heights))
        return len([1 for i in range(len(heights)) if sh[i] != heights[i]])
    
    
s = Solution()
print(s.heightChecker([1,1,4,2,1,3]))