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
created by shhuan at 2019/12/3 21:25

"""


from typing import List

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        a, b = 0, 1
        for i in range(1, len(A)):
            na, nb = float('inf'), float('inf')
            if A[i] > A[i-1] and B[i] > B[i-1]:
                na = a
                nb = b + 1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                na = min(na, b)
                nb = min(nb, a+1)
            a, b = na, nb

        return min(a, b)


s = Solution()
print(s.minSwap([0,4,4,5,9], [0,1,6,8,10]))
print(s.minSwap(A = [1,3,5,4], B = [1,2,3,7]))
print(s.minSwap([2,4,5,7,10], [1,3,4,5,9]))