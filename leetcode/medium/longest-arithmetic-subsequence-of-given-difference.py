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
created by shhuan at 2019/12/22 21:53

"""

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        A, N = arr, len(arr)
        maxl = collections.defaultdict(int)
        for i in range(N-1, -1, -1):
            v = A[i]
            maxl[v] = maxl[v+difference] + 1

        return max(maxl.values())

s = Solution()
print(s.longestSubsequence([4,12,10,0,-2,7,-8,9,-9,-12,-12,8,8], 0))
print(s.longestSubsequence(arr = [1,2,3,4], difference = 1))
print(s.longestSubsequence(arr = [1,3,5,7], difference = 1))
print(s.longestSubsequence(arr = [1,5,7,8,5,3,4,2,1], difference = -2))
print(s.longestSubsequence([-1,4,4,9,-1,6,7,9,1], -3))
