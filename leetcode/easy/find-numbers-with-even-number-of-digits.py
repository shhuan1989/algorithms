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
created by shhuan at 2019/12/22 10:30

"""


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def klen(v):
            k = 0
            while v > 0:
                v //= 10
                k += 1

            return k% 2==0

        return len([x for x in nums if klen(x)])

s = Solution()
print(s.findNumbers([12,345,2,6,7896]))