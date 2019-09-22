# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/22 21:17

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
    def subarrayBitwiseORs(self, A):
        ans = set()
        cur = {0}
        for x in A:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)
