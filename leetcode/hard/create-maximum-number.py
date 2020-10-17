# -*- coding: utf-8 -*-

"""
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]

f[i][j][l] 表示nums1的前i个数字，nums2的前j个数字，组成的长度最l的数字的最大值

f[i][j][l] = max { f[i-1][j][l], f[i][j-1][l], f[i-1][j][l-1]*10+nums1[i-1], f[i][j-1][l-1]*10+nums2[j-1]}

TLE



"""
__author__ = 'huash'

import sys
import os
import time
import collections
from typing import List
import bisect

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def prep(nums, k):
            drop = len(nums) - k
            out = []
            for num in nums:
                while drop and out and out[-1] < num:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in a+b]

        return max(merge(prep(nums1, i), prep(nums2, k-i))
                   for i in range(k+1)
                   if i <= len(nums1) and k-i <= len(nums2))

if __name__ == '__main__':
    s = Solution()
    # print(s.maxNumber([6, 7], [6, 0, 4], 5))
    # print(s.maxNumber([3, 9], [8, 9], 3))
    print(s.maxNumber([8,9], [3,9], 3))