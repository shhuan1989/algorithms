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
created by shhuan at 2017/11/8 18:21

"""


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        A = nums
        N = len(A)


        def nth_num(A, idx):

            p = A[0]
            l = 0
            n = len(A)
            r = n-1

            while l < r:
                while l < r and A[r] >= p:
                    r -= 1
                while l < r and A[l] < p:
                    l += 1
                A[l], A[r] = A[r], A[l]

            A[l] = p

            if l == idx:
                return p
            elif l > idx:
                return nth_num(A[:l], idx)
            else:
                return nth_num(A[l:], idx-l-1)

        median = nth_num(A, N//2)


        idx = [(2*i+1)%(N|1) for i in range(N)]
        i, j, k = 0, 0, N-1
        while j <= k:
            if A[j] > median:
                A[idx[i]], A[idx[j]] = A[idx[j]], A[idx[i]]
                i += 2
                j += 1
            elif A[j] < median:
                A[idx[j]], A[idx[k]] = A[idx[k]], A[idx[j]]
                k -= 1
            else:
                j += 1

        print(A)


s = Solution()
print(s.wiggleSort([1,3,2,2,3,1]))
print(s.wiggleSort([1,5,1,1,6,4]))
print(s.wiggleSort([1,2,2,1,2,1,1,1,1,2,2,2]))


