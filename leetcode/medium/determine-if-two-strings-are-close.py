# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/11/15 10:35

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        wca = collections.Counter(word1)
        wcb = collections.Counter(word2)
        wca = [c for w, c in wca.items()]
        wcb = [c for w, c in wcb.items()]
        wca.sort()
        wcb.sort()

        sa = list(sorted(set(word1)))
        sb = list(sorted(set(word2)))

        return wca == wcb and sa == sb


if __name__ == '__main__':
    s = Solution()
    print(s.closeStrings('abc', 'bca'))
    print(s.closeStrings('a', 'aa'))
    print(s.closeStrings('cabbba', 'abbccc'))
    print(s.closeStrings('cabbba', 'aabbss'))
    print(s.closeStrings("uau", "ssx"))