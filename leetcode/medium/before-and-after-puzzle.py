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
created by shhuan at 2019/12/24 23:29

"""


class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:

        ans = set()
        phrases = [x.split(' ') for x in phrases]
        for i, a in enumerate(phrases):
            for j in range(len(phrases)):
                if i == j:
                    continue
                b = phrases[j]
                if a[-1] == b[0]:
                    ans.add(' '.join(a+b[1:]))

        return list(sorted(ans))

s = Solution()
print(s.beforeAndAfterPuzzles(['a', 'b', 'a']))
print(s.beforeAndAfterPuzzles(["mission statement","a quick bite to eat","a chip off the old block","chocolate bar","mission impossible","a man on a mission","block party","eat my words","bar of soap"]))