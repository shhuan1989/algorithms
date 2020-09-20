# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/16 10:33

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
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        for i in range(len(arr)-2):
            if all([v % 2 == 1 for v in arr[i: i+3]]):
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.threeConsecutiveOdds([2, 6, 4, 1]))
    print(s.threeConsecutiveOdds([1, 3]))
    print(s.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))