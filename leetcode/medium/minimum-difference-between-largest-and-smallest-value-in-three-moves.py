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
created by shhuan at 2020/7/12 12:31

"""


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0

        nums.sort()

        ans = nums[-1] - nums[0]
        for left in range(4):
            right = 3 - left
            ans = min(ans, abs(nums[-1-right] - nums[left]))

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minDifference([5, 3, 2, 4]))
    print(s.minDifference([1, 5, 0, 10, 14]))
    print(s.minDifference([6, 6, 0, 1, 1, 4, 6]))
    print(s.minDifference([1, 5, 6, 14, 15]))
