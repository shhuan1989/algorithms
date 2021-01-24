# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/11/29 10:31

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
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(x) for x in accounts])

if __name__ == '__main__':
    s = Solution()
    print(s.maximumWealth([[1, 2, 3], [3, 2, 1]]))