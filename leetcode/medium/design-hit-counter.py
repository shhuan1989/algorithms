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
created by shhuan at 2019/12/22 11:50

"""


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = []

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if not self.hits:
            self.hits.append((timestamp, 1))
        elif self.hits[-1][0] == timestamp:
            self.hits[-1] = (timestamp, self.hits[-1][1] + 1)
        else:
            self.hits.append((timestamp, 1))

        while self.hits[0][0] < timestamp - 5 * 60:
            self.hits.pop(0)


    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """

        i = bisect.bisect_left(self.hits, (timestamp-5*60, float('inf')))
        ans = sum([c for t, c in self.hits[i:]])
        return ans


h = HitCounter()
h.hit(1)
h.hit(2)
h.hit(3)
print(h.getHits(4))
h.hit(300)
print(h.getHits(300))
print(h.getHits(301))