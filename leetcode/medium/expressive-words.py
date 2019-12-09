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
created by shhuan at 2019/12/8 21:30

"""

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:

        def chcount(word):
            wc = []
            pv, c = '', 0
            for i, v in enumerate(word):
                if v == pv:
                    c += 1
                else:
                    wc.append((pv, c))
                    pv = v
                    c = 1
            wc.append((pv, c))

            return wc

        wcs = chcount(S)

        def canexp(word):
            wc = chcount(word)

            if len(wcs) != len(wc):
                return False

            for a, b in zip(wcs, wc):
                if a[0] != b[0]:
                    return False
                if a[1] != b[1]:
                    if a[1] < b[1] or a[1] < 3:
                        return False

            return True

        return len([1 for w in words if canexp(w)])


s = Solution()
print(s.expressiveWords('heeellooo', ["hello", "hi", "helo"]))