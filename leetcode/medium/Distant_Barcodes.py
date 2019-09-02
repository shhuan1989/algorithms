# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/2 22:15

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        wc = collections.Counter(barcodes)
        wc = [(-c, w) for w, c in wc.items()]
        wc.sort()

        q = []
        for c, w in wc:
            q += [w] * (-c)

        ans = [None for _ in range(len(barcodes))]
        ans[::2] = q[:len(ans[::2])]
        ans[1::2] = q[len(ans[::2]):]

        return ans



s = Solution()
# print(s.rearrangeBarcodes([1,1,1,1,2,2,3,3]))
print(s.rearrangeBarcodes([51,83,51,40,51,40,51,40,83,40,83,83,51,40,40,51,51,51,40,40,40,83,51,51,40,51,51,40,40,51,51,40,51,51,51,40,83,40,40,83,51,51,51,40,40,40,51,51,83,83,40,51,51,40,40,40,51,40,83,40,83,40,83,40,51,51,40,51,51,51,51,40,51,83,51,83,51,51,40,51,40,51,40,51,40,40,51,51,51,40,51,83,51,51,51,40,51,51,40,40]))