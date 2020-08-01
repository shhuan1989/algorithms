# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/7/25 22:41

"""

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        pre = target[0]
        ans = 0
        for i in range(1, len(target)):
            v = target[i]
            if v < pre:
                ans += pre-v
            pre = v

        return ans + pre
    
if __name__ == '__main__':
    s = Solution()
    print(s.minNumberOperations([1, 2, 3, 2, 1]))
    print(s.minNumberOperations([3, 1, 1, 2]))
    print(s.minNumberOperations([3, 1, 5, 4, 2]))
    print(s.minNumberOperations([1, 1, 1, 1]))

    A = [random.randint(0, 10**5) for _ in range(10**5)]
    t0 = time.time()
    print(s.minNumberOperations(A))
    print(time.time() - t0)