# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2019/11/17 13:11

"""


from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = 0
        odds = [i for i, v in enumerate(nums) if v % 2 != 0]
        for i in range(len(odds)-k+1):
            j = i + k - 1
            l = odds[i] - odds[i-1] if i > 0 else odds[i] + 1
            r = odds[j+1] - odds[j] if j < len(odds) - 1 else N - odds[j]
            ans += l * r

        return ans


s = Solution()
print(s.numberOfSubarrays(nums = [1,1,2,1,1], k = 3))
print(s.numberOfSubarrays(nums = [2,4,6], k = 1))
print(s.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))


