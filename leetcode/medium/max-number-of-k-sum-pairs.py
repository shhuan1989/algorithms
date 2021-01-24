# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/12/6 10:32

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
    def maxOperations(self, nums: List[int], k: int) -> int:

        wc = collections.Counter(nums)

        ans = 0
        for u in wc.keys():
            v = k - u
            if u == v:
                ans += wc[u] // 2
                wc[u] = 0
            elif v in wc:
                d = min(wc[u], wc[v])
                wc[u] -= d
                wc[v] -= d
                ans += d

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maxOperations([1,2 , 3, 4], 5))
    print(s.maxOperations([3, 1, 3, 4, 3], 6))