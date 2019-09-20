# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/13 23:07

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        N = len(persons)
        A = [-1 for _ in range(N)]
        wc = collections.defaultdict(int)
        winner = -1
        maxv = -1
        for i, p in enumerate(persons):
            wc[p] += 1

            if wc[p] >= maxv:
                winner = p
                maxv = wc[p]

            A[i] = winner

        self.A = A
        self.T = times
        self.N = N


    def q(self, t: int) -> int:
        i = bisect.bisect_left(self.T, t)
        if i < self.N and self.T[i] == t:
            return self.A[i]

        return self.A[i-1]



# s = TopVotedCandidate([0,1,1,0,0,1,0],[0,5,10,15,20,25,30])
# for t in [3, 12, 25, 15, 24, 8]:
#     print(s.q(t))

s = TopVotedCandidate([0,0,0,0,1],[0,6,39,52,75])
for t in [44, 49, 59, 68, 42, 37, 99, 26, 78, 43]:
    print(s.q(t))