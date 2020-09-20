# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/23 10:40

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
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)
        return sum(piles[1:n//3*2:2])


if __name__ == '__main__':
    s = Solution()
    print(s.maxCoins([2, 4, 1, 2, 7, 8]))
    print(s.maxCoins([2, 4, 5]))
    print(s.maxCoins([9,8,7,6,5,1,2,3,4]))