# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/2

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution(object):
    def shortestSubarray(self, A, K):
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        #Want smallest y-x with Py - Px >= K
        ans = N+1 # N+1 is impossible
        monoq = collections.deque() #opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            #Want opt(y) = largest x with Px <= Py - K
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N+1 else -1
    
    
s = Solution()
print(s.shortestSubarray([17, 85, 93, -45, -21],  150))
# print(s.shortestSubarray([1], 1))
# print(s.shortestSubarray([1, 2], 4))
# print(s.shortestSubarray([2, -1, 2], 3))