# -*- coding: utf-8 -*-

"""
created by shhuan at 2021/1/3 10:41

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
    def waysToSplit(self, nums: List[int]) -> int:

        presum = [0]
        for v in nums:
            presum.append(presum[-1] +  v)

        mod = 10**9+7

        ans = 0
        n = len(nums)
        # print(presum)
        for i in range(1, n+1):
            if presum[-1] < 3 * presum[i]:
                break
            x = presum[i]
            left = max(bisect.bisect_left(presum, 2 * x), i + 1)
            right = bisect.bisect_right(presum, (presum[-1] + x) // 2)

            ans += max(0, right - left)
            # print(i, left, right, ans)
            ans %= mod

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.waysToSplit([7,2,5,5,6,2,10,9]))
    print(s.waysToSplit([5,10,1,10,4]))
    print(s.waysToSplit([2,3,5,10]))
    print(s.waysToSplit([1, 1, 1]))
    print(s.waysToSplit([1,2,2,2,5,0]))
    print(s.waysToSplit([3, 2, 1]))