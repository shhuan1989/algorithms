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
created by shhuan at 2019/12/15 22:14

"""

class Solution:
    def countTriplets(self, A: List[int]) -> int:
        N = len(A)
        s = collections.defaultdict(int)
        for i in range(N):
            for j in range(N):
                s[A[i] & A[j]] += 1

        ans = 0
        for k, v in s.items():
            for u in A:
                if k & u == 0:
                    ans += v
        return ans

s = Solution()
print(s.countTriplets([2, 1, 3]))

