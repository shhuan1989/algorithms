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
created by shhuan at 2019/12/18 22:29

"""

class Solution:
    def minSwaps(self, data: List[int]) -> int:

        K = sum(data)
        s = sum(data[:K])
        ans = s
        for i in range(K, len(data)):
            s += data[i] - data[i-K]
            ans = max(ans, s)
        return K-ans

s = Solution()
print(s.minSwaps([1, 0, 1, 0, 1]))
print(s.minSwaps([0, 0, 0, 1, 0]))
print(s.minSwaps([1,0,1,0,1,0,0,1,1,0,1]))
