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
created by shhuan at 2019/12/7 18:23

"""

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        wc = collections.Counter(A + B)
        possible = [w for w, c in wc.items() if c >= N]

        ans = N + 1
        for a, b in [[A, B], [B, A]]:
            for w in possible:
                c = 0
                for i in range(N):
                    if a[i] != w:
                        if b[i] == w:
                            c += 1
                        else:
                            c = N+1
                            break
                ans = min(ans, c)

        return ans if ans <= N else -1


s = Solution()
print(s.minDominoRotations(A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]))
print(s.minDominoRotations(A = [3,5,1,2,3], B = [3,6,3,3,4]))
