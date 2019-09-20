# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/18 20:12

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1, N + 1):
            s = bin(i)[2:]
            print(s)
            if S.find(s) < 0:
                return False

        return True

s = Solution()
# print(s.queryString("0110", 4))
print(s.queryString("1111000101", 5))