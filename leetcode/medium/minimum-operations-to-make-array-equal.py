# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/16 10:35

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


class Solution:
    def minOperations(self, n: int) -> int:

        if n % 2 == 0:
            return  n * n // 4
        else:
            return  n // 2 * (n + 1) // 2


if __name__ == '__main__':
    s = Solution()
    print(s.minOperations(3))
    print(s.minOperations(6))
    print(s.minOperations(1))