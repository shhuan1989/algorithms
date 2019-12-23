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
created by shhuan at 2019/12/19 20:42

"""


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        for i in range(N-1):
            if (i % 2 == 0) == (nums[i] > nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]