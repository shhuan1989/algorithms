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
created by shhuan at 2019/12/19 00:46

"""


class Solution:
    def groupStrings(self, s: List[str]) -> List[List[str]]:
        if not s:
            return []

        OA = ord('a')
        def rep(word):
            d = (26 - (ord(word[0]) - OA)) % 26
            return ''.join([chr((ord(ch) + d - OA) % 26 + OA) for ch in word])

        ans = collections.defaultdict(list)
        for w in s:
            ans[rep(w)].append(w)

        return list(ans.values())

s = Solution()
print(s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))




