# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/19/20

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
        if n <= 0:
            return 0
        
        v = n
        a = []
        while v > 0:
            a.append(v % 10)
            v //= 10
        a = a[::-1]
        na = len(a)
        
        
        @lru_cache(maxsize=None)
        def count(s, i, less):
            if i >= na:
                return 1
            if (s & (1 << i)) > 0:
                # set this bit to 1 if v less than a
                if less:
                    return count(s, i+1, less)
                else:
                    if a[i] > 1:
                        return count(s, i+1, True)
                    elif a[i] == 1:
                        return count(s, i+1, less)
                    else:
                        return 0
            else:
                if less:
                    return 9 * count(s, i+1, less)
                else:
                    v = a[i]
                    if v == 0:
                        return count(s, i+1, False)
                    if v == 1:
                        return count(s, i + 1, True)
                    else:
                        return (v - 1) * count(s, i + 1, True) + count(s, i + 1, False)
                        
        
        def ones(val):
            x = 0
            while val > 0:
                x += val & 1
                val >>= 1
            return x
        
        
        ans = 0
        for i in range(1, 1 << na):
            ans += count(i, 0, False) * ones(i)
        
        return ans
        
        
        
        


s = Solution()
print(s.countDigitOne(12))
print(s.countDigitOne(11))
print(s.countDigitOne(13))
print(s.countDigitOne(10))
print(s.countDigitOne(21))