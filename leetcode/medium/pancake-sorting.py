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
created by shhuan at 2019/12/18 22:21

"""


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:

        ans = []

        N = len(A)
        while N > 1:
            maxv, maxi = float('-inf'), -1
            for i in range(N):
                if A[i] > maxv:
                    maxi = i
                    maxv = A[i]
            if maxi == N-1:
                N -= 1
                A.pop()
                continue

            if maxi > 0:
                ans.append(maxi + 1)
            ans.append(N)
            N -= 1
            A[:maxi + 1] = A[:maxi + 1][::-1]
            A = A[::-1]
            A.pop()

        return ans

s = Solution()
print(s.pancakeSort([3, 2, 4, 1]))