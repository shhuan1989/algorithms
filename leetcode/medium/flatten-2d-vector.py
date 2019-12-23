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
created by shhuan at 2019/12/19 17:29

"""


class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.data = []
        for u in v:
            self.data.extend(u)
        self.index = 0

    def next(self) -> int:
        ans = self.data[self.index]
        self.index += 1
        return ans

    def hasNext(self) -> bool:
        return self.index < len(self.data)

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()