# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/2 10:32

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
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n-1:
            return max(arr)

        premax = [0]
        for v in arr:
            premax.append(max(premax[-1], v))

        for i,v in enumerate(arr):
            if i == 0:
                if v >= premax[min(i+k+1, n)]:
                    return v
            else:
                if v > premax[i] and v >= premax[min(i + k, n)]:
                    return v


if __name__ == '__main__':
    s = Solution()
    print(s.getWinner(arr = [2,1,3,5,4,6,7], k = 2))
    print(s.getWinner(arr = [3,2,1], k = 10))
    print(s.getWinner(arr = [1,9,8,2,3,7,6,4,5], k = 7))
    print(s.getWinner(arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000))