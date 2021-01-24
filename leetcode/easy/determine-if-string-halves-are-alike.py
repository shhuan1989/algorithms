# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/12/27 10:30

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
    def halvesAreAlike(self, s: str) -> bool:

        s = s.lower()
        n = len(s)
        a = s[:n//2]
        b = s[n//2:]

        ow = {'a', 'e', 'i', 'o', 'u'}
        ca = len([x for x in a if x in ow])
        cb = len([x for x in b if x in ow])

        return ca == cb


if __name__ == '__main__':
    s = Solution()
    print(s.halvesAreAlike('book'))
    print(s.halvesAreAlike('textbook'))
    print(s.halvesAreAlike('MerryChristmas'))
    print(s.halvesAreAlike('AbCdEfGh'))