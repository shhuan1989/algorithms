# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2019/12/3 20:49

"""

from typing import List
from functools import lru_cache

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)

        N = len(words)
        dp = [0] * N
        wi = {}
        for i, w in enumerate(words):
            pl = 0
            for j in range(len(w)):
                pw = w[:j] + w[j+1:]
                if pw in wi:
                    pl = max(pl, dp[wi[pw]])

            dp[i] = pl + 1
            wi[w] = i

        return max(dp)




s = Solution()
print(s.longestStrChain(["a","b","ba","bca","bda","bdca"]))

words = []
for i in range(1000):
    w = ''
    for l in range(1, random.randint(2, 16)):
        c = random.randint(0, 25)
        c = chr(c + ord('a'))
        w += c
    words.append(w)
t0 = time.time()
print(s.longestStrChain(words))
print(time.time() - t0)

