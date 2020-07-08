# -*- coding: utf-8 -*-
"""


Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.


"""
import collections
import time
from typing import List
import bisect

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        a = list(sorted(nums))
        n = len(nums)
        bit = [0 for _ in range(n)]
        
        def query(index):
            c = 0
            while index >= 0:
                c += bit[index]
                index = (index & (index + 1)) - 1
            return c
            
        def update(index):
            while index < n:
                bit[index] += 1
                index |= index+1
            
        ans = 0
        for i, v in enumerate(nums):
            ans += i - query(bisect.bisect_right(a, v * 2)-1)
            update(bisect.bisect_left(a, v))
            
        return ans
    

    def reversePairs_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def merge(a, b):
            c = []
            l = 0
            r = 0
            while l < len(a) and r < len(b):
                if a[l] <= b[r]:
                    c.append(a[l])
                    l += 1
                else:
                    c.append(b[r])
                    r += 1
            return c + a[l:] + b[r:]

        def merge_sort(vals):
            if not vals:
                return [], 0

            if len(vals) == 1:
                return vals, 0

            mid = len(vals) // 2

            left, lrvp = merge_sort(vals[:mid])
            right, rrvp = merge_sort(vals[mid:])

            rvp = lrvp + rrvp
            l = 0
            r = 0
            count = 0

            # 核心统计方法
            while l < len(left):
                if r >= len(right) or left[l] <= 2 * right[r]:
                    l += 1
                    rvp += count
                else:
                    r += 1
                    count += 1

            return merge(left, right), rvp

        return merge_sort(nums)[1]

s = Solution()
print(s.reversePairs([]))
print(s.reversePairs([2,4,3,5,1]))