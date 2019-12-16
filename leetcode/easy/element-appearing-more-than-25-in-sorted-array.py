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
created by shhuan at 2019/12/14 22:30

"""


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        wc = collections.Counter(arr)
        N = len(arr)
        for k, c in wc.items():
            if c * 4 > N:
                return k
        return -1