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
created by shhuan at 2020/1/11 22:30

"""


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        N = len(nums)
        for i in range(0, N, 2):
            ans.extend([nums[i+1]] * nums[i])
        return ans


s = Solution()
print(s.decompressRLElist([1, 2, 3, 4]))
print(s.decompressRLElist([]))