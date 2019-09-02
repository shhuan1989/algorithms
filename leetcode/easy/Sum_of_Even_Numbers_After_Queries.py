# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/1 15:30

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
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        csum = sum([x for x in A if x % 2 == 0])
        ans = []
        for v, i in queries:
            ov = A[i]
            A[i] += v
            nv = A[i]

            if ov % 2 == 0 and nv % 2 ==0:
                csum += nv - ov
            elif ov % 2 == 0 and nv % 2 != 0:
                csum -= ov
            elif ov % 2 != 0 and nv % 2 == 0:
                csum += nv

            ans.append(csum)

        return ans