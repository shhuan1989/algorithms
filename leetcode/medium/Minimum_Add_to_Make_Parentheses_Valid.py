# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/1 15:40

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
    def minAddToMakeValid(self, S: str) -> int:

        c = 0
        ans = 0
        for v in S:
            if v == ')':
                c -= 1
                if c < 0:
                    ans += abs(c)
                    c = 0
            else:
                c += 1

        return ans + c