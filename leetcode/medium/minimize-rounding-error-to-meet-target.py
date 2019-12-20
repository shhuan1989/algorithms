# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/19/19

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
    def minimizeError(self, prices: List[str], target: int) -> str:
        prices = [float(v) for v in prices]
        minv = sum([int(v) for v in prices])
        maxv = sum([int(math.ceil(v)) for v in prices])
        
        if target < minv or target > maxv:
            return '-1'
        
        up = target-minv
        
        diff = [(v-int(v), i) for i, v in enumerate(prices)]
        diff.sort(reverse=True)
        
        upi = {i for v, i in diff[:up]}
        
        ans = 0
        for i in upi:
            v = prices[i]
            ans += math.ceil(v) - v
        
        for i in range(len(prices)):
            if i not in upi:
                v = prices[i]
                ans += v - math.floor(v)
            
        return '{:.3f}'.format(ans)
    
s = Solution()
print(s.minimizeError(prices = ["0.700","2.800","4.900"], target = 8))







        
        