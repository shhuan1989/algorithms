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
created by shhuan at 2019/12/3 20:30

"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l = []
        s = list(s)
        for i, v in enumerate(s):
            if v == '(':
                l.append(i)
            elif v == ')':
                if l:
                    l.pop()
                else:
                    s[i] = ''

        for i in l:
            s[i] = ''

        return ''.join(s)


s = Solution()
print(s.minRemoveToMakeValid(s = "lee(t(c)o)de)"))
print(s.minRemoveToMakeValid(s = "a)b(c)d"))
print(s.minRemoveToMakeValid(s = "))(("))
print(s.minRemoveToMakeValid(s = "(a(b(c)d)"))
