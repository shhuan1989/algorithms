# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/2/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        wc = collections.Counter(arr)
        wc = [(c, w) for w, c in wc.items()]
        wc.sort(reverse=True)
        
        ans = 0
        count = 0
        for c, w in wc:
            if count * 2 >= len(arr):
                break
            count += c
            ans += 1
        return ans
    
    
s = Solution()
print(s.minSetSize(arr = [3,3,3,3,5,5,5,2,2,7]))
print(s.minSetSize([7,7,7,7,7,7]))
print(s.minSetSize([1,9]))
print(s.minSetSize([1000,1000,3,7]))
print(s.minSetSize([1,2,3,4,5,6,7,8,9,10]))
print(s.minSetSize([]))
        
