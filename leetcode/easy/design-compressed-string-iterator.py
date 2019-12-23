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
created by shhuan at 2019/12/22 17:46

"""


class StringIterator:

    def __init__(self, compressedString: str):
        s, r = [], 0
        while r < len(compressedString):
            if compressedString[r].isalpha():
                ci = r + 1
                while ci < len(compressedString) and compressedString[ci].isdigit():
                    ci += 1
                s.append((compressedString[r], int(compressedString[r+1: ci])))
                r = ci
        self.s = s
        self.i = 0
        self.j = 0

    def next(self) -> str:
        if self.j < self.s[self.i][1]:
            self.j += 1
            return self.s[self.i][0]
        elif self.i + 1 < len(self.s):
            self.j = 1
            self.i += 1
            return self.s[self.i][0]
        return ' '

    def hasNext(self) -> bool:
        if self.j < self.s[self.i][1]:
            return True

        return self.i < len(self.s)-1


s = StringIterator('')
for a, b in zip(["StringIterator","next","next","next","hasNext","next","next","next","next","next","next","next","hasNext","next","next","next","next","next","hasNext","next","next","next","next","next","hasNext","next","next","next","next","hasNext","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","hasNext","next","hasNext","next","next","next","next","next","next","hasNext","next","next","next","next","next","next","next","next","next","next","next","next","next","next","hasNext","next","next","next","hasNext","next","next","hasNext","next","next","next","next","next"], [["x6"],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]):
    if a == 'StringIterator':
        s = StringIterator(b[0])
    elif a == 'hasNext':
        print(s.hasNext())
    else:
        print(s.next())