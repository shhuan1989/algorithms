# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/6 10:34

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
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = collections.defaultdict(int)
        p2 = collections.defaultdict(int)
        for v in nums1:
            p1[v**2] += 1
        for v in nums2:
            p2[v**2] += 1

        ans = 0
        n1 = len(nums1)
        for i in range(n1):
            for j in range(i+1, n1):
                u = nums1[i] * nums1[j]
                ans += p2[u]

        n2 = len(nums2)
        for i in range(n2):
            for j in range(i+1, n2):
                u = nums2[i] * nums2[j]
                ans += p1[u]

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numTriplets(nums1 = [7,4], nums2 = [5,2,8,9]))
    print(s.numTriplets([1, 1], [1, 1, 1]))
    print(s.numTriplets(nums1 = [7,7,8,3], nums2 = [1,2,9,7]))
    print(s.numTriplets(nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]))
