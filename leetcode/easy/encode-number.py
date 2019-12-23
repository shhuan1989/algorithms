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
created by shhuan at 2019/12/22 00:39

"""

class Solution:
    def encode(self, num: int) -> str:
        return bin(num+1)[3:]

s = Solution()
print(s.encode(23))