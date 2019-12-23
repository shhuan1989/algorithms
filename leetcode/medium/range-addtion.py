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
created by shhuan at 2019/12/19 03:25

"""

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        A = [0] * (length + 1)
        for u, v, w in updates:
            A[u] += w
            A[v+1] -= w

        s = 0
        ans = []
        for i in range(length):
            s += A[i]
            ans.append(s)

        return ans

s = Solution()
print(s.getModifiedArray(5, [[1,3,2],[2,4,3],[0,2,-2]]))