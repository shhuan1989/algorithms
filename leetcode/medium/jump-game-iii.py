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
created by shhuan at 2019/12/29 10:35

"""


class Solution:
    def canReach(self, A: List[int], start: int) -> bool:
        if A[start] == 0:
            return True

        N = len(A)
        riched = [False for _ in range(N)]
        riched[start] = True
        q = [start]
        while q:
            a = q.pop()
            if A[a] == 0:
                return True

            for i in [a + A[a], a - A[a]]:
                if 0 <= i < N and not riched[i]:
                    riched[i] = True
                    q.append(i)

        return False

s = Solution()
print(s.canReach(A = [4,2,3,0,3,1,2], start = 5))
print(s.canReach(A = [4,2,3,0,3,1,2], start = 0))
print(s.canReach(A = [3,0,2,1,2], start = 2))
print(s.canReach([0,3,0,6,3,3,4], 6))



