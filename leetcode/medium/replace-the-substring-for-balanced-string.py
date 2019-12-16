# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2019/12/10 20:41

"""

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        ch = ['Q', 'W', 'E', 'R']
        idx = {v:i for i, v in enumerate(ch)}
        counts = [s.count(c) for c in ch]
        rm = [c-n//4 for c in counts]

        if all([c <= 0 for c in rm]):
            return 0

        l, r = 0, 0
        rmd = [0] * 4
        ans = n
        while r < n:
            v = s[r]
            iv = idx[v]
            rmd[iv] += 1
            if rmd[iv] >= rm[iv] and all([rmd[j] >= rm[j] for j in range(4)]):
                ans = min(ans, r-l+1)
                while l <= r:
                    ans = min(ans, r-l+1)
                    isl = idx[s[l]]
                    rmd[isl] -= 1
                    if rmd[isl] < rm[isl]:
                        l += 1
                        break
                    l += 1
            r += 1
        return ans


s = Solution()
print(s.balancedString('WQWRQQQW'))
print(s.balancedString('QWER'))
print(s.balancedString('QQWE'))
print(s.balancedString('QQQW'))
print(s.balancedString('QQQQ'))