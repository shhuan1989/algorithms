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
    def numOfSubarrays(self, arr: List[int]) -> int:

        presum = [0]
        for v in arr:
            presum.append(presum[-1] + v)

        ans = 0
        MOD = 10**9+7

        odd = 0
        even = 0
        for v in presum:
            if v % 2 == 0:
                even += 1
                ans += odd
                ans %= MOD
            else:
                odd += 1
                ans += even
                ans %= MOD

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.numOfSubarrays([1, 3, 5]))
    print(s.numOfSubarrays([2, 4, 6]))
    print(s.numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))
    print(s.numOfSubarrays([100, 100, 99, 99]))
    print(s.numOfSubarrays([7]))