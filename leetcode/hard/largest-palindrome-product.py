# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/27 20:25

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


class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 9
        if n == 2:
            return 987

        for a in range(2, 9 * 10 ** (n - 1)):
            hi = (10 ** n) - a
            lo = int(str(hi)[::-1])
            if a ** 2 - 4 * lo < 0:
                continue
            if (a ** 2 - 4 * lo) ** .5 == int((a ** 2 - 4 * lo) ** .5):
                return (lo + 10 ** n * (10 ** n - a)) % 1337
