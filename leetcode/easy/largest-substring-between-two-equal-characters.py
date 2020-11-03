# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        pre = {}
        ans = -1
        for i, c in enumerate(s):
            if c in pre:
                ans = max(ans, i - pre[c] - 1)
            else:
                pre[c] = i
        
        return ans
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.maxLengthBetweenEqualCharacters('aa'))
    print(s.maxLengthBetweenEqualCharacters('abca'))
    print(s.maxLengthBetweenEqualCharacters('cbzxy'))
    print(s.maxLengthBetweenEqualCharacters('cabbac'))