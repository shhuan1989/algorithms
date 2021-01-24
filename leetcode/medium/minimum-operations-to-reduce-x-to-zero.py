# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/11/15 10:38

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
    def minOperations(self, nums: List[int], x: int) -> int:

        presum = [0]
        for v in nums:
            presum.append(presum[-1] + v)


        n = len(nums)
        ans = n + 1
        for a in range(n+1):
            pre = presum[a]
            if pre > x:
                break
            if pre == x:
                ans = min(ans, a)
            b = x - pre
            bi = bisect.bisect_right(presum, presum[-1] - b)
            if a < bi-1 <= n and presum[-1] - presum[bi-1] == b:
                ans= min(ans, a + n - bi + 1)

        return ans if ans <= n else -1

if __name__ == '__main__':
    s = Solution()
    # print(s.minOperations([1, 1, 4, 2, 3], 5))
    # print(s.minOperations([5, 6, 7, 8, 9], 4))
    # print(s.minOperations([3, 2, 20, 1, 1, 3], 10))
    print(s.minOperations([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], 134365))


