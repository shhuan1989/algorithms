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
created by shhuan at 2019/12/21 23:48

"""

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:

        wi = collections.defaultdict(list)
        for i, v in enumerate(S):
            wi[v].append(i)

        def check(w):
            pos = 0
            for i, v in enumerate(w):
                j = bisect.bisect_left(wi[v], pos)
                if 0 <= j < len(wi[v]):
                    pos = max(pos+1, wi[v][j] + 1)
                else:
                    return False
            return True

        return len([w for w in words if check(w)])

s = Solution()
print(s.numMatchingSubseq('abcde', ['a', 'bb', 'acd', 'ace']))