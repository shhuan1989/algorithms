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
import math

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        
        ans = []
        diff = num + 100
        for i in range(1, int(math.sqrt(num+2))+2):
            for v in [num+1, num+2]:
                a = v // i
                if a * i == v:
                    print(i, a)
                    if abs(a-i) < diff:
                        diff = abs(a-i)
                        ans = [i, a]
        return ans
    
s = Solution()
print(s.closestDivisors(1))
# print(s.closestDivisors(8))
# print(s.closestDivisors(10**9))
# print(s.closestDivisors(123))
        