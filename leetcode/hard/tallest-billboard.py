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
created by shhuan at 2019/12/2 22:55

"""

from typing import List
class Solution(object):
    def tallestBillboard(self, rods):
        def make(A):
            states = {(0, 0)}
            for x in A:
                states |= ({(a+x, b) for a, b in states} |
                           {(a, b+x) for a, b in states})

            delta = {}
            for a, b in states:
                delta[a-b] = max(delta.get(a-b, 0), a)
            return delta

        N = len(rods)
        Ldelta = make(rods[:N//2])
        Rdelta = make(rods[N//2:])

        ans = 0
        for d in Ldelta:
            if -d in Rdelta:
                ans = max(ans, Ldelta[d] + Rdelta[-d])
        return ans


s = Solution()
print(s.tallestBillboard([1, 2, 3, 6]))
print(s.tallestBillboard([1,2,3,4,5,6]))
print(s.tallestBillboard([1, 2]))
t0 = time.time()
print(s.tallestBillboard([1,2,4,8,16,32,64,128,256,512,50,50,50,150,150,150,100,100,100,123]))
print(time.time() - t0)