# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/9 10:41

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
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        presum = [0]
        for v in nums:
            presum.append(presum[-1] + v)

        vi = collections.defaultdict(list)
        for i, v in enumerate(presum):
            vi[v].append(i)


        segs = collections.defaultdict(list)
        for i, v in enumerate(presum):
            for j in vi[v+target]:
                if j > i:
                    segs[j].append(i)

        N = len(nums)
        dp = [0 for _ in range(N+2)]
        for i in range(1, N+2):
            dp[i] = max(dp[i], dp[i-1])
            for j in segs[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.maxNonOverlapping([1, 1, 1, 1, 1,], 2))
    print(s.maxNonOverlapping(nums = [-1,3,5,1,4,2,-9], target = 6))
    print(s.maxNonOverlapping( [-2,6,6,3,5,4,1,2,8], target = 10))
    print(s.maxNonOverlapping(nums = [0,0,0], target = 0))