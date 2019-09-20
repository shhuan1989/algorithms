# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/5 00:14

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
    def brokenCalc(self, X: int, Y: int) -> int:
        if Y <= X:
            return X-Y
        if Y % 2 == 0:
            return 1 + self.brokenCalc(X, Y // 2)

        return 1 + self.brokenCalc(X, Y+1)