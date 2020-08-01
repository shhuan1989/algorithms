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
created by shhuan at 2020/7/25 22:38

"""

class Solution:
    def numSplits(self, s: str) -> int:
        wc = collections.Counter(s)
        left = set()
        right = len(wc)
        ans = 0
        for i, c in enumerate(s):
            left.add(c)
            wc[c] -= 1
            if wc[c] <= 0:
                right -= 1

            if len(left) == right:
                ans += 1

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.numSplits('aacaba'))
    print(s.numSplits('abcd'))
    print(s.numSplits('aaaaa'))
    print(s.numSplits('acbadbaada'))