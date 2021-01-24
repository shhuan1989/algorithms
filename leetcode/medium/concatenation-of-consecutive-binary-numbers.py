# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/12/6 10:35

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
    def concatenatedBinary(self, n: int) -> int:

        ans = ''.join(map(str, [bin(i)[2:] for i in range(1, n+1)]))
        return int(ans, 2) % (10**9+7)


if __name__ == '__main__':
    s = Solution()
    print(s.concatenatedBinary(1))
    print(s.concatenatedBinary(3))
    print(s.concatenatedBinary(12))