# -*- coding: utf-8 -*-

"""
created by shhuan at 2021/1/3 10:30

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
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        a = [[-v, w] for w, v in boxTypes]
        a.sort()
        ans = 0
        i = 0
        while truckSize > 0 and i < len(a):
            v, w = a[i]
            x = min(w, truckSize)
            truckSize -= x
            ans -= x * v
            i += 1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4))
    print(s.maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10))