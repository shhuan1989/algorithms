# -*- coding:utf-8 -*-

"""
created by shuangquan.huang at 2021/1/21
"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        pre = list(itertools.accumulate(nums))
        ans = 0
        for i in range(n):
            l = max(i + 1, bisect_left(pre, pre[i] + pre[i]))
            r = min(n - 1, bisect_right(pre, (pre[i] + pre[-1]) // 2))
            ans = (ans + max(0, r - l)) % mod
        return ans % mod


if __name__ == '__main__':
    s = Solution()
    print(s.waysToSplit([7, 2, 5, 5, 6, 2, 10, 9]))
    print(s.waysToSplit([5, 10, 1, 10, 4]))
    print(s.waysToSplit([2, 3, 5, 10]))
    print(s.waysToSplit([1, 1, 1]))
    print(s.waysToSplit([1, 2, 2, 2, 5, 0]))
    print(s.waysToSplit([3, 2, 1]))
