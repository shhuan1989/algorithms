# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/2 10:30

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
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N = len(arr)
        ans = 0
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        ans += 1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countGoodTriplets([3,0,1,1,9,7], a = 7, b = 2, c = 3))
    print(s.countGoodTriplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1))