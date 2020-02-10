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
    def minTaps(self, n: int, ranges: List[int]) -> int:
        a = [i for i in range(n+1)]
        for i in range(n+1):
            l = max(0, i-ranges[i])
            r = min(n, i+ranges[i])
            a[l] = max(a[l], r)
        
        left, right = 0, 0
        i = 0
        ans = 0
        while i <= n:
            if i > right:
                return -1
            ans += 1
            while i <= left:
                right = max(right, a[i])
                i += 1
            if right >= n:
                return ans
            
            if left == right:
                return -1
            left = right
            
                
            
            
    
    
s = Solution()
print(s.minTaps(n = 5, ranges = [3,4,1,1,0,0]))
print(s.minTaps(3, [0, 0, 0, 0]))
print(s.minTaps(n = 7, ranges = [1,2,1,0,2,1,0,1]))
print(s.minTaps(n = 8, ranges = [4,0,0,0,0,0,0,0,4]))
print(s.minTaps(n = 8, ranges = [4,0,0,0,4,0,0,0,4]))



            