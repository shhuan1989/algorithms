# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/22 21:38

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List


class Solution(object):
    def decodeAtIndex(self, S, K):
        size = 0
        # Find size = length of decoded string
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1