# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/29/19

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
print(s.shortestSubarray([1], 1))
print(s.shortestSubarray([1, 2], 4))
print(s.shortestSubarray([2, -1, 2], 3))
print(s.shortestSubarray([84,-37,32,40,95], 167))
print(s.shortestSubarray([48,99,37,4,-31], 140))
print(s.shortestSubarray([77,19,35,10,-14], 19))
print(s.shortestSubarray([-34,37,51,3,-12,-50,51,100,-47,99,34,14,-13,89,31,-14,-44,23,-38,6], 151))

        