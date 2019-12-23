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
created by shhuan at 2019/12/22 11:24

"""

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        if abs(ns-nt) > 1:
            return False
        if s == t:
            return False

        if ns < nt:
            s, t = t, s
            ns, nt = nt, ns
        si, ti = 0, 0
        diff = 0
        while si < ns:
            if ti >= nt or s[si] != t[ti]:
                diff += 1
                si += 1
                if ns == nt:
                    ti += 1
            else:
                si += 1
                ti += 1

        return diff == 1

s = Solution()
print(s.isOneEditDistance('a', ''))
print(s.isOneEditDistance('ab', 'acb'))
print(s.isOneEditDistance('cab', 'ad'))
print(s.isOneEditDistance('1203', '1213'))
