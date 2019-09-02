# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/8/25 11:19

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = collections.defaultdict(list)
        self.cap = capacity
        self.avb = {0}
        self.dv = set()
        self.maxid = 0

    def push(self, val: int) -> None:
        if not self.avb:
            self.maxid += 1
            i = self.maxid
            self.avb.add(i)
        else:
            i = min(self.avb)

        s = self.stacks[i]
        if len(s) >= self.cap:
            self.maxid += 1
            s = self.stacks[i]

        s.append(val)
        if len(s) >= self.cap:
            self.avb.remove(i)
        self.dv.add(i)

    def pop(self) -> int:
        ans = -1
        if not self.dv:
            return ans

        i = max(self.dv)
        ans = self.stacks[i].pop()
        if not self.stacks[i]:
            self.dv.remove(i)
            del self.stacks[i]

        return ans

    def popAtStack(self, index: int) -> int:
        s = self.stacks[index]
        ans = -1
        if s:
            ans = s.pop()
            if not s:
                self.dv.discard(index)
                del self.stacks[index]
            self.avb.add(index)

        return ans

s = DinnerPlates(2)
for v in [1, 2, 3, 4, 5]:
    s.push(v)
print(s.popAtStack(0))
s.push(20)
s.push(21)
print(s.popAtStack(0))
print(s.popAtStack(2))
for i in range(5):
    print(s.pop())