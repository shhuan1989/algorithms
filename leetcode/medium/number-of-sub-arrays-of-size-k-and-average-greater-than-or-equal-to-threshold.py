# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/10/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if not arr or len(arr) < k:
            return 0
    
        t = k * threshold
        
        s = sum(arr[:k])
        ans = 1 if s >= t else 0
        for i in range(k, len(arr)):
            s -= arr[i-k]
            s += arr[i]
            ans += 1 if s >= t else 0
            
        return ans
    
s = Solution()
print(s.numOfSubarrays([2,2,2,2,5,5,5,8], k = 3, threshold = 4))
print(s.numOfSubarrays([1,1,1,1,1], k = 1, threshold = 0))
print(s.numOfSubarrays([11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))
print(s.numOfSubarrays([7,7,7,7,7,7,7], k = 7, threshold = 7))
print(s.numOfSubarrays([4,4,4,4], k = 4, threshold = 1))
