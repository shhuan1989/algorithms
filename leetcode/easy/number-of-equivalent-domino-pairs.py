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
created by shhuan at 2019/12/24 22:39

"""


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum([v*(v-1)//2 for v in collections.Counter([''.join(map(str, sorted(d))) for d in dominoes]).values()])

s = Solution()
print(s.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))