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
created by shhuan at 2019/12/24 22:20

"""


class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        us = {}

        def find(u):
            if u not in us or us[u] == u:
                return u
            pu = find(us[u])
            us[u] = pu
            return pu

        def union(u, v):
            pu, pv = find(u), find(v)
            us[pu] = pv

        for a, b in pairs:
            union(a, b)

        return all([find(a) == find(b) for a, b in zip(words1, words2)])


s = Solution()
print(s.areSentencesSimilarTwo(["great","acting","skills"],
                               ["fine","drama","talent"],
                               [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]))