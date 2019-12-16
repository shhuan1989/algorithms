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
created by shhuan at 2019/12/10 22:38

"""

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        N = len(fronts)
        wc = collections.Counter(fronts + backs)
        same = {a for a, b in zip(fronts, backs) if a == b}
        for v in sorted([k for k, v in wc.items() if v <= N and k not in same]):
            if len([1 for a, b in zip(fronts, backs) if a != v or b != v]) == N:
                return v

        return 0

s = Solution()
print(s.flipgame(fronts = [1,2,4,4,7], backs = [1,3,4,1,3]))