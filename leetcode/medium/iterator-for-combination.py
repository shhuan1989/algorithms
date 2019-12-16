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
created by shhuan at 2019/12/14 22:36

"""


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):

        def dfs(s, i, c, pre):
            if c == 0:
                return [pre]

            if i >= len(s) or c < 0 or len(s)-i+1 < c:
                return []

            return dfs(s, i+1, c-1, pre + s[i]) + dfs(s, i+1, c, pre)

        self.data = list(sorted(dfs(characters, 0, combinationLength, '')))
        self.index = 0

    def next(self) -> str:
        i = self.index
        self.index += 1
        return self.data[i]

    def hasNext(self) -> bool:
        return self.index < len(self.data)


s = CombinationIterator('abc', 2)
print(s.next())
print(s.next())
print(s.next())
print(s.hasNext())
# print(s.next())