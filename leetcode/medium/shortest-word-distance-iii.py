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
created by shhuan at 2019/12/22 23:18

"""


class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        wi = collections.defaultdict(list)
        for i, w in enumerate(words):
            wi[w].append(i)

        if word2 == word1:
            idx = wi[word1]
            return min([abs(a-b) for a, b in zip(idx[:-1], idx[1:])])

        ia, ib = wi[word1], wi[word2]
        ans = float('inf')
        for i in ia:
            l, r = bisect.bisect_left(ib, i-1), bisect.bisect_right(ib, i + 1)
            if 0 <= r < len(ib):
                ans = min(ans, abs(ib[r] - i))
            if r > 0:
                ans = min(ans, abs(ib[r-1] - i))
            if 0 <= l < len(ib):
                ans = min(ans, abs(i - ib[l]))
                if l + 1 < len(ib):
                    ans = min(ans, abs(i - ib[l+1]))

        return ans

s = Solution()
print(s.shortestWordDistance( ["practice", "makes", "perfect", "coding", "makes"], 'makes', 'coding'))




