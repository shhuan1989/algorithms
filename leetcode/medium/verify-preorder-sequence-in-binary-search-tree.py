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
created by shhuan at 2019/12/24 22:07

"""


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        s = []
        minVal = float('-inf')
        for v in preorder:
            if v < minVal:
                return False
            if not s or v < s[-1]:
                s.append(v)
            else:
                while s and v > s[-1]:
                    minVal = max(minVal, s.pop())
                s.append(v)

        return True


s = Solution()
print(s.verifyPreorder([5, 2, 6, 1, 3]))
print(s.verifyPreorder([5, 2, 1, 3, 6]))
print(s.verifyPreorder([1, 3, 4, 2]))