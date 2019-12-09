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
created by shhuan at 2019/12/8 10:31

"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a, b = 1, 0
        while n > 0:
            c = n % 10
            n //= 10
            a *= c
            b += c

        return a - b

s = Solution()
print(s.subtractProductAndSum(234))
print(s.subtractProductAndSum(4421))
print(s.subtractProductAndSum(1))