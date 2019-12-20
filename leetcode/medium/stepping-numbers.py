# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/20/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        
        def dfs(val):
            if val > high:
                return []
            
            ans = []
            if val >= low:
                ans.append(val)
                
            last = val % 10
            if last + 1 < 10:
                ans.extend(dfs(val * 10 + (last+1)))
            if last - 1 >= 0:
                ans.extend(dfs(val * 10 + (last - 1)))
            
            return ans
        
        ans = []
        for i in range(1, 10):
            ans.extend(dfs(i))
            
        if low <= 0 <= high:
            ans.append(0)
        
        return list(sorted(set(ans)))
        
        
        
        

s = Solution()
print(s.countSteppingNumbers(10, 15))
# print(s.countSteppingNumbers(0, 21))
# print(s.countSteppingNumbers(0, 10**9))
print(s.countSteppingNumbers(0, 1000000000))
