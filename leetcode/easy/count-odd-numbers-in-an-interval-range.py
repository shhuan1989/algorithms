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
created by shhuan at 2020/7/25 22:30

"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low > high:
            return 0

        if low % 2 == 0:
            return (high - low + 1) // 2
        else:
            return (high - low + 2) // 2


s = Solution()
print(s.countOdds(3, 10))
print(s.countOdds(3, 11))
print(s.countOdds(4, 10))
print(s.countOdds(4, 11))
print(s.countOdds(5, 5))