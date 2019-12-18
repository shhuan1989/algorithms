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
created by shhuan at 2019/12/19 00:37

"""


class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        x = []

        ns = len(s)
        for w in dict:
            nw = len(w)
            for i in range(ns - nw + 1):
                if s[i: i+nw] == w:
                    x.append((i, i+nw))

        mark = [False] * ns
        for a, b in x:
            for c in range(a, b):
                mark[c] = True

        ans = ''
        m = False
        for i in range(ns):
            if mark[i] and not m:
                m = True
                ans += '<b>'
            elif not mark[i] and m:
                m = False
                ans += '</b>'
            ans += s[i]
        if mark[-1]:
            ans += '</b>'

        return ans

s = Solution()
print(s.addBoldTag(s = "abcxyz123", dict = ["abc","123"]))
print(s.addBoldTag(s = "aaabbcc", dict = ["aaa","aab","bc"]))