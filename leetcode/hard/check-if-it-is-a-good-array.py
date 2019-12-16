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
created by shhuan at 2019/12/15 21:46

"""

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        import math

        a = nums[0]
        for i in range(1, len(nums)):
            a = math.gcd(a, nums[i])
            if a == 1:
                return True
        return a == 1