# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/26

https://oi-wiki.org/dp/number/

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
    def countDigitOne(self, n: int) -> int:
        
        @lru_cache(maxsize=None)
        def ncr(c, r):
            if r == 0:
                return 1
            
            if c < r:
                return 0
            if c == r:
                return 1
            
            if r == 1:
                return c
            
            return ncr(c-1, r) + ncr(c-1, r-1)
        
        def pre(bits, ones):
            count = 0
            for i in range(bits+1):
                count += i * ncr(bits, i) * (9 ** (bits-i))
            count += ones * (10**bits)
            return count
        
        digits = []
        v = n
        while v > 0:
            digits.append(v % 10)
            v //= 10

        def dfs(i, st, op):
            if i <= 0:
                return st
            
            if op == 1:
                # less than current val
                return pre(i, st)
            else:
                # equal with current val
                cur = digits[i-1]
                ans = dfs(i-1, st + (1 if cur == 1 else 0), 0)
                for u in range(cur):
                    ans += dfs(i-1, st + (1 if u == 1 else 0), 1)
                
                return ans
        
        i = len(digits)
        ans = dfs(i-1, 1 if digits[-1] == 1 else 0, 0)
        for v in range(digits[-1]):
            ans += dfs(i-1, 1 if v == 1 else 0, 1)
            
        return ans
    
    def brutal(self, n: int) -> int:
        ans = 0
        
        def cal(val):
            c = 0
            while val > 0:
                c += 1 if val % 10 == 1 else 0
                val //= 10
            return c
        
        for i in range(n+1):
            ans += cal(i)
        
        return ans
    
s = Solution()

for i in range(1, 1000):
    if s.brutal(i) != s.countDigitOne(i):
        print(i, s.brutal(i), s.countDigitOne(i))