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
created by shhuan at 2019/12/19 01:00

"""

class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        N = len(S)
        if K > N:
            return 0
        presum = [collections.defaultdict(int)]
        pre = presum[0]

        for i, v in enumerate(S):
            c = pre.copy()
            c[v] += 1
            presum.append(c)
            pre = c

        ans = 0
        for i in range(N-K+1):
            c, d = presum[i], presum[i+K]
            e = [v-c[k] for k, v in d.items()]
            if all([v <= 1 for v in e]):
                ans += 1

        return ans

s = Solution()
print(s.numKLenSubstrNoRepeats('havefunonleetcode', 5))
print(s.numKLenSubstrNoRepeats('home', 5))