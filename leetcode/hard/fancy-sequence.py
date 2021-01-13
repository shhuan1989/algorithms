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
        self.mul = [1 for _ in range(MAXN)]
        self.add = [0 for _ in range(MAXN)]
        self.index = 0

    def append(self, val: int) -> None:
        self.data[self.index] = val
        self.index += 1
        self.mul[self.index] = self.mul[self.index-1]
        self.add[self.index] = self.add[self.index-1]


    def addAll(self, inc: int) -> None:
        self.add[self.index] += inc

    def multAll(self, m: int) -> None:
        self.mul[self.index] *= m
        self.add[self.index] *= m
        self.mul[self.index] %= MOD
        self.add[self.index] %= MOD

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
        a = self.inv(self.mul[idx]) * self.mul[self.index]
        b = (self.add[self.index] - self.add[idx] * a + MOD) % MOD
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