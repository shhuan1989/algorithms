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
created by shhuan at 2019/12/22 18:05

"""


class WordDistance:

    def __init__(self, words: List[str]):
        wi = collections.defaultdict(list)
        for i, w in enumerate(words):
            wi[w].append(i)
        self.wi = wi

    def shortest(self, word1: str, word2: str) -> int:
        wi = self.wi
        ia, ib = wi[word1], wi[word2]
        ans = float('inf')
        for i in ia:
            j = bisect.bisect_left(ib, i)
            for k in range(max(0, j-2), min(len(ib), j+2)):
                ans = min(ans, abs(i-ib[k]))
        return ans


wd = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
print(wd.shortest('coding', 'practice'))
print(wd.shortest('makes', 'coding'))