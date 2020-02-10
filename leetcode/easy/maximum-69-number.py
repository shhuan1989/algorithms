# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/19/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def maximum69Number (self, num: int) -> int:
        a = []
        while num > 0:
            a.append(num % 10)
            num //= 10
            
        a = a[::-1]
        for i, v in enumerate(a):
            if v == 6:
                a[i] = 9
                break
        
        ans = 0
        for v in a:
           ans *= 10
           ans +=v
        
        return ans
    
    
s = Solution()
print(s.maximum69Number(669))
print(s.maximum69Number(9669))
print(s.maximum69Number(6))
print(s.maximum69Number(9))
print(s.maximum69Number(9996))
print(s.maximum69Number(9999))