# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/16 10:45

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
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()

        def check(force):
            pre = position[0]
            count = 1
            for v in position[1:]:
                if v - pre >= force:
                    pre = v
                    count += 1
            return count >= m

        lo, hi = 0, position[-1] - position[0]
        while lo <= hi:
            force = (lo + hi) // 2
            if check(force):
                lo = force + 1
            else:
                hi = force - 1

        return hi


if __name__ == '__main__':
    s = Solution()
    # print(s.maxDistance([1, 2, 3, 4, 7], 3))
    # print(s.maxDistance([5, 4, 3, 2, 1, 10000000], 2))
    print(s.maxDistance([79,74,57,22], 4))