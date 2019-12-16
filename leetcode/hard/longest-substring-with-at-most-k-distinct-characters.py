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
created by shhuan at 2019/12/15 22:57

"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        l, r = 0, 0
        wc = {}
        ans = 0
        while r < len(s):
            v = s[r]
            if v not in wc:
                wc[v] = 1
            else:
                wc[v] +=1

            if len(wc.keys()) > k:
                while l < r:
                    u = s[l]
                    wc[u] -= 1
                    l += 1
                    if wc[u] == 0:
                        del wc[u]
                        break

            else:
                ans = max(ans, r-l+1)
            r += 1

        return ans

s = Solution()
print(s.lengthOfLongestSubstringKDistinct('eceba', 2))
print(s.lengthOfLongestSubstringKDistinct('aa', 1))