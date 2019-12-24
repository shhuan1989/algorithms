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
created by shhuan at 2019/12/23 19:02

"""

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1

        ns1, ns2 = [],  []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                ns1.append(s1[i])
                ns2.append(s2[i])

        c1 = len([i for i in range(len(ns1)) if ns1[i] == 'x' and ns2[i] == 'y'])
        c2 = len([i for i in range(len(ns1)) if ns1[i] == 'y' and ns2[i] == 'x'])

        d = c1 % 2 + c2 % 2
        if d == 1:
            return -1
        else:
            return c1 // 2 + c2 // 2 + d

s = Solution()
print(s.minimumSwap('xx', 'yy'))
print(s.minimumSwap('xy', 'yx'))
print(s.minimumSwap('xx', 'xy'))
print(s.minimumSwap('xxyyxyxyxx', 'xyyxyxxxyx'))



