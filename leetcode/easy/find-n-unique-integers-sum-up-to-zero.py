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
created by shhuan at 2019/12/29 10:30

"""


class Solution:
    def sumZero(self, n: int) -> List[int]:

        a = 1
        ans = []
        for i in range(n // 2):
            ans.append(a)
            ans.append(-a)
            a += 1

        if n % 2 == 1:
            ans.append(0)
        return ans


s = Solution()
print(s.sumZero(3))
print(s.sumZero(1))
print(s.sumZero(4))