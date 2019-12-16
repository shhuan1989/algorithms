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
created by shhuan at 2019/12/14 11:32

"""

class Solution(object):
    def wordsAbbreviation(self, words):
        def abbrev(word, i = 0):
            if (len(word) - i <= 3):
                return word
            return word[:i+1] + str(len(word) - i - 2) + word[-1]

        N = len(words)
        ans = list(map(abbrev, words))
        prefix = [0] * N

        for i in range(N):
            while True:
                dupes = set()
                for j in range(i+1, N):
                    if ans[i] == ans[j]:
                        dupes.add(j)

                if not dupes:
                    break
                dupes.add(i)
                for k in dupes:
                    prefix[k] += 1
                    ans[k] = abbrev(words[k], prefix[k])

        return ans


s = Solution()
print(s.wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]))
print(["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"])
