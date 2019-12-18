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
created by shhuan at 2019/12/19 00:32

"""

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        A = [0] * (n+2)
        for a, b, c in bookings:
            A[a] += c
            A[b+1] -= c

        ans = [0] * (n+1)
        s = 0
        for i in range(1, n+1):
            s += A[i]
            ans[i] = s

        return ans[1:]

s = Solution()
print(s.corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5))
