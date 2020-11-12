# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/10/19 20:37

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


MAXN = 10**5 + 5
MOD = 10**9 + 7

class Fancy:

    def __init__(self):
        self.data = [0 for _ in range(MAXN)]
        self.a = [1 for _ in range(MAXN)]
        self.b = [0 for _ in range(MAXN)]
        self.index = 0

    def append(self, val: int) -> None:
        self.data[self.index] = val
        self.index += 1
        self.a[self.index] = self.a[self.index-1]
        self.b[self.index] = self.b[self.index-1]


    def addAll(self, inc: int) -> None:
        self.b[self.index] += inc

    def multAll(self, m: int) -> None:
        self.a[self.index] *= m
        self.b[self.index] *= m

    def mypow(self, a, p):
        ans = 1
        b = a
        for i in range(32):
            if p & (1 << i) > 0:
                ans *= b
                ans %= MOD
            b *= b
            b %= MOD

        return ans

    def inv(self, a):
        return self.mypow(a, MOD-2)

    def getIndex(self, idx: int) -> int:
        if idx >= self.index:
            return -1
        a = self.inv(self.a[idx]) * self.a[self.index]
        b = (self.b[self.index] - self.b[idx] * a + MOD) % MOD
        return (a * self.data[idx] + b) % MOD


if __name__ == '__main__':
    f = Fancy()
    f.append(2)
    f.addAll(3)
    f.append(7)
    f.multAll(2)
    print(f.getIndex(0))
    f.addAll(3)
    f.append(10)
    f.multAll(2)
    print(f.getIndex(0))
    print(f.getIndex(1))
    print(f.getIndex(2))