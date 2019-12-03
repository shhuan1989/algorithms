# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2019/12/2 22:06

"""

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        N = len(arr)
        cz = [0] * N
        for i in range(N):
            cz[i] = (cz[i - 1] if i > 0 else 0) + (1 if arr[i] == 0 else 0)

        shift, lastz = 0, False
        for i in range(N):
            r = i + cz[i]
            if r == N - 1:
                shift = cz[i]
                break
            elif r > N - 1:
                shift = cz[i] - 1
                lastz = True
                break

        r = N - 1
        for i in range(N-shift-1, -1, -1):
            if arr[i] == 0:
                arr[r] = 0
                r -= 1
                if not (lastz and i == N-shift-1):
                    arr[r] = 0
                    r -= 1
            else:
                arr[r] = arr[i]
                r -= 1
        print(arr)

s = Solution()
print(s.duplicateZeros([8,4,5,0,0,0,0,7]))
print(s.duplicateZeros([1,0,2,3,0,4,5,0]))