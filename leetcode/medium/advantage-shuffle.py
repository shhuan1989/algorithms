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
created by shhuan at 2019/12/11 23:41

"""

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A)
        B = [(v, i) for i, v in enumerate(B)]
        B.sort()
        A.sort()

        used = []
        ignored = []
        ia = 0
        for i, (b, ib) in enumerate(B):
            while ia < N and A[ia] <= b:
                ignored.append(A[ia])
                ia += 1

            if ia >= N:
                break

            used.append((A[ia], ib))
            ia += 1

        ans = [0] * N
        filled = [False] * N
        for v, i in used:
            ans[i] = v
            filled[i] = True

        for v, i in zip(ignored, [i for i in range(N) if not filled[i]]):
            ans[i] = v
        return ans

s = Solution()
# print(s.advantageCount(A = [2,7,11,15], B = [1,10,4,11]))
# print(s.advantageCount(A = [12,24,8,32], B = [13,25,32,11]))
# print(s.advantageCount([2,0,4,1,2], [1,3,0,0,2]))