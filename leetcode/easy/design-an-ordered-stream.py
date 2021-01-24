# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/11/15 10:30

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


class OrderedStream:

    def __init__(self, n: int):
        self.data = ['' for _ in range(n+1)]
        self.ptr = 1
        self.n = n


    def insert(self, id: int, value: str) -> List[str]:
        self.data[id] = value
        if id == self.ptr:
            ans = []
            i = id
            while i <= self.n and self.data[i]:
                ans.append(self.data[i])
                i += 1
            self.ptr = i
            return ans
        return []

if __name__ == '__main__':
    s = OrderedStream(5)
    print(s.insert(3, 'ccc'))
    print(s.insert(1, 'aaa'))
    print(s.insert(2, 'bbb'))
    print(s.insert(5, 'eee'))
    print(s.insert(4, 'ddd'))

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)