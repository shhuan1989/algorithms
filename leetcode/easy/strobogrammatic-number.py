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
created by shhuan at 2019/12/18 23:48

"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if any([v not in {'0', '1', '6', '8', '9'} for v in num]):
            return False
        if len(num) == 1 and num in {'6', '9'}:
            return False
        l, r = 0, len(num) - 1
        while l < r:
            if num[l] not in {'6', '9'}:
                if num[l] != num[r]:
                    return False
            else:
                if '{}{}'.format(num[l], num[r]) not in {'69', '96'}:
                    return False

            l += 1
            r -= 1

        return True

s = Solution()
print(s.isStrobogrammatic('66'))