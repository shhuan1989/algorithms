# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/24/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        
        pairs = {
            '1': '1',
            '0': '0',
            '8': '8',
            '6': '9',
            '9': '6'
        }
        
        low, high = int(low), int(high)
        
        def dfs(val):
            num = int(val + ''.join([pairs[v] for v in reversed(val)]))
            if num > high:
                return 0
            
            ans = 0
            if low <= num <= high:
                ans += 1
            
            for v in ['0', '1', '8']:
                num = int(val + v + ''.join([pairs[v] for v in reversed(val)]))
                if low <= num <= high:
                    ans += 1
            
            for v in ['0', '1', '6', '8', '9']:
                ans += dfs(val+v)
            
            return ans
        
        ans = 0
        for v in ['1', '6', '8', '9']:
            ans += dfs(v)
        
        for v in [0, 1, 8]:
            if low <= v <= high:
                ans += 1
        
        return ans
    
s = Solution()
print(s.strobogrammaticInRange('50', '100'))
print(s.strobogrammaticInRange('0', '0'))
print(s.strobogrammaticInRange('0', '1'))


