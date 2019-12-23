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
created by shhuan at 2019/12/22 11:48

"""


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re

        a = re.split('\W+', paragraph.lower())
        wc = collections.Counter(a)
        wc = [(c, w) for w, c in wc.items()]
        wc.sort(reverse=True)

        banned = set(banned)
        for c, w in wc:
            if w not in banned:
                return w

s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", banned=['hit']))