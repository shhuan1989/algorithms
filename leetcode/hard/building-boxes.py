# -*- coding:utf-8 -*-

"""
created by shuangquan.huang at 2021/1/24
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


class Solution:
    def minimumBoxes(self, n: int) -> int:
        a = [x*(x+1)//2 for x in range(1, 10000)]
        presum = [0]
        for v in a:
            presum.append(presum[-1] + v)
        
        for i in range(len(presum)):
            if presum[i] == n:
                return a[i-1]
            if presum[i] < n < presum[i+1]:
                y = presum[i]
                z = n - y
                v = 1
                while v * (v + 1) // 2 < z:
                    v += 1
                return a[i-1] + v

        
if __name__ == '__main__':
    s = Solution()
    print(s.minimumBoxes(3))
    print(s.minimumBoxes(4))
    print(s.minimumBoxes(10))
    print(s.minimumBoxes(15))
    print(s.minimumBoxes(10**9))