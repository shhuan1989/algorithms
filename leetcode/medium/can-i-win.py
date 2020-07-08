# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/29

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

from functools import lru_cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal > maxChoosableInteger * (maxChoosableInteger + 1) // 2:
            return False
        
        @lru_cache(maxsize=None)
        def dfs(digits, target):
            if digits == 0:
                return False
            
            return any(digits & (1 << i) for i in range(max(target - 1, 0), maxChoosableInteger)) or \
                   any(digits & (1 << i) and not dfs(digits ^ (1 << i), target - i - 1) for i in range(target - 1))
        
        return dfs((1 << maxChoosableInteger) - 1, desiredTotal)


s = Solution()
print(s.canIWin(3, 0))
print(s.canIWin(5, 50))
print(s.canIWin(4, 6))
print(s.canIWin(10, 11))
print(s.canIWin(10, 40))
print(s.canIWin(18, 79))
