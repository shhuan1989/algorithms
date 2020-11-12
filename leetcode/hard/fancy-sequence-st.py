# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/10/19 21:05

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

class SegmentTree:
    def __init__(self, size):
        self.n = size * 4
        self.size = size
        self.data = [0 for _ in range(self.n)]
        self.lazya = [1 for _ in range(self.n)]
        self.lazyb = [0 for _ in range(self.n)]

    def push(self, index):

        if self.lazya[index] > 1:
            self.data[index] *= self.lazya[index]
            self.data[index] %= MOD
            if index * 2 + 2 < self.n:
                self.lazya[index * 2 + 1] *= self.lazya[index]
                self.lazya[index * 2 + 1] %= MOD
                self.lazya[index * 2 + 2] *= self.lazya[index]
                self.lazya[index * 2 + 2] %= MOD
                self.lazyb[index * 2 + 1] *= self.lazya[index]
                self.lazyb[index * 2 + 1] %= MOD
                self.lazyb[index * 2 + 2] *= self.lazya[index]
                self.lazyb[index * 2 + 2] %= MOD

            self.lazya[index] = 1

        if self.lazyb[index] > 0:
            self.data[index] += self.lazyb[index]
            self.data[index] %= MOD
            if index * 2 + 2 < self.n:
                self.lazyb[index * 2 + 1] += self.lazyb[index]
                self.lazyb[index * 2 + 1] %= MOD
                self.lazyb[index * 2 + 2] += self.lazyb[index]
                self.lazyb[index * 2 + 2] %= MOD
            self.lazyb[index] = 0

    def update(self, index, val):
        self.update_impl(0, 0, self.size-1, index, index, val)

    def update_impl(self, index, nodel, noder, targetl, targetr, val):
        if nodel > targetr or noder < targetl:
            return

        if nodel == targetl and noder == targetr:
            self.data[index] = val
            return

        mid = (nodel + noder) // 2
        self.update_impl(index * 2 + 1, nodel, mid, targetl, min(targetr, mid), val)
        self.update_impl(index * 2 + 2, mid+1, noder, max(targetl, mid+1), targetr, val)


    def query(self, index):
        return self.query_impl(0, 0, self.size-1, index, index)

    def query_impl(self, index, nodel, noder, targetl, targetr):
        self.push(index)
        if nodel == targetl and noder == targetr:
            return self.data[index]

        mid = (nodel + noder) // 2

        if targetr <= mid:
            return self.query_impl(index * 2 + 1, nodel, mid, targetl, targetr)
        else:
            return self.query_impl(index * 2 + 2, mid+1, noder, targetl, targetr)

    def mult(self, m, index):
        self.mult_impl(0, 0, self.size-1, 0, index, m)

    def mult_impl(self, index, nodel, noder, targetl, targetr, val):
        self.push(index)
        if nodel > targetr or noder < targetl:
            return

        if nodel == targetl and noder == targetr:
            self.lazya[index] *= val
            return

        mid = (nodel + noder) // 2
        self.mult_impl(index * 2 + 1, nodel, mid, targetl, min(targetr, mid), val)
        self.mult_impl(index * 2 + 2, mid+1, noder, max(targetl, mid+1), targetr, val)

    def add(self, m, index):
        self.add_impl(0, 0, self.size-1, 0, index, m)

    def add_impl(self, index, nodel, noder, targetl, targetr, val):
        self.push(index)
        if nodel > targetr or noder < targetl:
            return

        if nodel == targetl and noder == targetr:
            self.lazyb[index] += val
            return

        mid = (nodel + noder) // 2
        self.add_impl(index * 2 + 1, nodel, mid, targetl, min(targetr, mid), val)
        self.add_impl(index * 2 + 2, mid+1, noder, max(targetl, mid+1), targetr, val)


class Fancy:

    def __init__(self):
        self.st = SegmentTree(MAXN)
        self.index = 0

    def append(self, val: int) -> None:
        self.st.update(self.index, val)
        self.index += 1


    def addAll(self, inc: int) -> None:
        self.st.add(inc, self.index-1)

    def multAll(self, m: int) -> None:
        self.st.mult(m, self.index-1)

    def getIndex(self, idx: int) -> int:
        return self.st.query(idx) if idx < self.index else -1


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