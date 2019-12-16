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
created by shhuan at 2019/12/11 23:54

"""


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        d = self.data[key]
        i = bisect.bisect_right(d, (timestamp, float('-inf')))
        if d and 0 < i <= len(d):
            return d[i-1]
        return ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)