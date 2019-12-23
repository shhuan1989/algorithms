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
created by shhuan at 2019/12/22 00:05

"""


class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.s = []
        self.t = []

    def push(self, x: int) -> None:

        self.s.append(x)
        if not self.t:
            self.t.append(0)
        else:
            pv, pi = self.s[self.t[-1]], self.t[-1]
            if pv > x:
                self.t.append(pi)
            else:
                self.t.append(len(self.s)-1)

    def pop(self) -> int:
        if not self.s:
            return -1
        ans = self.s.pop()
        self.t.pop()
        return ans

    def top(self) -> int:
        return self.s[-1] if self.s else - 1

    def peekMax(self) -> int:
        return self.s[self.t[-1]] if self.t else -1

    def popMax(self) -> int:
        if not self.t:
            return -1
        i = self.t[-1]
        ans = self.s[i]
        self.s = self.s[:i] + self.s[i+1:]
        pi = 0
        self.t = []
        for i, v in enumerate(self.s):
            if v >= self.s[pi]:
                self.t.append(i)
                pi = i
            else:
                self.t.append(pi)

        return ans


s = MaxStack()
s.push(5)
s.push(1)
s.push(-5)
print(s.popMax())
print(s.popMax())
print(s.top())