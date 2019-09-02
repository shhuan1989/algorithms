# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/8/25 10:44

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        def f(w):
            wc = collections.Counter(w)
            return wc[min(list(w))]

        fw = [f(w) for w in words]
        fw.sort()
        qw = [f(w) for w in queries]

        ans = []
        for a in qw:
            ans.append(len(fw)-bisect.bisect_right(fw, a))

        return ans


s = Solution()
print(s.numSmallerByFrequency(queries = ["cbd"], words = ["zaaaz"]))
print(s.numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]))