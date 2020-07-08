# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/7

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        a = max(left or [0])
        b = max([n-v for v in right] or [0])
        
        return max(a, b)
    

if __name__ == '__main__':
    s = Solution()
    print(s.getLastMoment(n = 7, left = [], right = [0,1,2,3,4,5,6,7]))
    print(s.getLastMoment(n = 7, left = [0,1,2,3,4,5,6,7], right = []))
    print(s.getLastMoment(n = 9, left = [5], right = [4]))
    print(s.getLastMoment(n = 6, left = [6], right = [0]))