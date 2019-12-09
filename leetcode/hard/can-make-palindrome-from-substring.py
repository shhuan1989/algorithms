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
created by shhuan at 2019/12/7 19:03

"""

class Solution:
    def canMakePaliQueries(self, s, queries):
        N = len(s)
        last, wcs = 0, [0 for _ in range(N+1)]
        for i, v in enumerate(s):
            last ^= (1 << (ord(v) - ord('a')))
            wcs[i+1] = last

        ans = [True for _ in range(len(queries))]
        for i, (l, r, t) in enumerate(queries):
            if t >= min(26, r-l+1) // 2:
                continue
            c, d = 0, wcs[q[0]] ^ wcs[q[1]+1]
            while d:
                d &= d-1
                c += 1
            # c = len([b for b in bin(wcs[r+1] ^ wcs[l]) if b == '1'])
            ans[i] = True if (t >= (c // 2)) else False

        return ans

s = Solution()
print(s.canMakePaliQueries(s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))
print(s.canMakePaliQueries("abcda", [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))
print(s.canMakePaliQueries("ninmjmj", [[6,6,0],[1,1,1],[2,5,4],[1,3,1],[5,6,1]]))
