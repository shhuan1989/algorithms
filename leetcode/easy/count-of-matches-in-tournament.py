# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/12/13 10:30

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
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            if n % 2 == 0:
                ans += n // 2
                n //= 2
            else:
                ans += (n-1) // 2
                n = (n-1) // 2 + 1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfMatches(7))
    print(s.numberOfMatches(14))