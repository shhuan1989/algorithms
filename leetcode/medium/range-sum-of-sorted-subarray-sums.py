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
created by shhuan at 2020/7/12 12:28

"""


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        presum = [0]
        for v in nums:
            presum.append(presum[-1] + v)

        a = []
        for i in range(n):
            for j in range(i, n):
                a.append(presum[j+1] - presum[i])

        a.sort()

        return sum(a[left-1: right])


if __name__ == '__main__':
    s = Solution()
    print(s.rangeSum([1, 2, 3, 4], 4, 1, 5))