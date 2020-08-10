# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/9 10:34

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
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        for i in range(1, n):
            s = s + '1' + ''.join(['1' if v == '0' else '0' for v in s][::-1])

        return s[k-1]


if __name__ == '__main__':
    s = Solution()
    print(s.findKthBit(3, 1))
    print(s.findKthBit(4, 11))
    print(s.findKthBit(1, 1))
    print(s.findKthBit(2, 3))
    print(s.findKthBit(20, 2**18))