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
created by shhuan at 2019/12/10 21:26

"""

class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        res = A[-1] - A[0] #情形一：全体加K或减K
        #情形2：排序后，在某个i的位置，i之前的较小的所有元素都加K，从i开始往后的所有较大的元素都减K
        for i in range(1, len(A)):  #但不确定哪个i是合理的，所以把所有i都算一下，选出最优的那个
            cmin = min(A[0] + K, A[i] - K)  #数组改变后，最小值只会是第一项或第i项；最大值只会是第i-1项或第-1项
            cmax = max(A[i-1] + K, A[-1] - K)
            res = min(res, cmax - cmin) #选出最优秀的res
        return res





s = Solution()
print(s.smallestRangeII([10,2,9,2,2,2], 5))
print(s.smallestRangeII([1, 3, 6], 3))
print(s.smallestRangeII([7, 8, 8, 5, 2], 4))
print(s.smallestRangeII([6, 6, 7, 6], 4))
print(s.smallestRangeII([7, 8, 8], 5))
print(s.smallestRangeII([1], 0))
print(s.smallestRangeII([0, 10], 2))
print(s.smallestRangeII([1, 3, 6], 3))