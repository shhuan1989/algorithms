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
created by shhuan at 2019/12/22 00:32

"""


class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:

        us = {}

        def find(u):
            if u not in us or us[u] == u:
                return u
            p = find(us[u])
            us[u] = p
            return p

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu > pv:
                us[pu] = pv
            else:
                us[pv] = pu

        for a, b in zip(A, B):
            union(a, b)

        return ''.join([find(u) for u in S])

s = Solution()
print(s.smallestEquivalentString(A = "parker", B = "morris", S = "parser"))
print(s.smallestEquivalentString(A = "hello", B = "world", S = "hold"))
print(s.smallestEquivalentString(A = "leetcode", B = "programs", S = "sourcecode"))





