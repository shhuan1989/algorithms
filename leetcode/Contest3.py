# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/9/24 09:55

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        A = nums
        if not A:
            return None

        N = len(A)
        lo = 0
        hi = N

        while lo < hi:
            m = (lo + hi) // 2

            if A[m] > A[lo]:
                if m >= N - 1:
                    return A[lo]
                elif A[m] > A[hi-1]:
                  lo = m + 1
                else:
                    hi = m
            else:
                if m > lo and A[m] < A[m-1]:
                    return A[m]
                elif A[m] < A[hi-1]:
                    hi = m
                else:
                    lo = m+1

        return A[lo-1]





s = Solution()
print(s.findMin([4, 5, 6, 7, 0, 1, 2, 3]))
print(s.findMin([1]))
print(s.findMin([1, 2, 3]))
print(s.findMin([2, 3, 0, 1]))
print(s.findMin([2, 3, 4, 0, 1]))
print(s.findMin([3, 4, 0, 1, 2]))