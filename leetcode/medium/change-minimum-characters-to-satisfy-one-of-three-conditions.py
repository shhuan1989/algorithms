# -*- coding:utf-8 -*-

"""
created by shuangquan.huang at 2021/1/24
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
    def minCharacters(self, a: str, b: str) -> int:
        n = len(a)
        a = [ord(x)-ord('a') for x in a]
        b = [ord(x)-ord('a') for x in b]
        ans = float('inf')
        # 1
        
        ca = []
        cb = []
        for x in range(26):
            ca.append(len([v for v in a if v > x]))
            cb.append(len([v for v in b if v < x]))
        
        for x in range(26):
            for y in range(x+1, 26):
                ans = min(ans, ca[x] + cb[y])
        
        # 2
        ca = []
        cb = []
        for x in range(26):
            ca.append(len([v for v in a if v < x]))
            cb.append(len([v for v in b if v > x]))
        for x in range(26):
            for y in range(x):
                ans = min(ans, ca[x] + cb[y])
                
        # 3
        for t in range(26):
            x = len([x for x in a if x != t]) + len([x for x in b if x != t])
            ans = min(ans, x)
            
        return ans
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.minCharacters('aba', 'caa'))
    print(s.minCharacters('dabadd', 'cda'))