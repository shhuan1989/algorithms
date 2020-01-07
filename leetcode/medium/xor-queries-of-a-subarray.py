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
created by shhuan at 2020/1/5 10:36

"""


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        N = len(arr)
        A = arr
        bit = [0 for _ in range(N)]

        def add(index, val):
            while index < N:
                bit[index] ^= val
                index |= index + 1

        def left(index):
            ans = 0
            while index >= 0:
                ans ^= bit[index]
                index = (index & (index + 1)) - 1

            return ans

        def query(l, r):
            return left(r) ^ left(l-1)

        for i, v in enumerate(A):
            add(i, v)

        ans = [query(l, r) for l, r in queries]
        return ans


s = Solution()
print(s.xorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]))
print(s.xorQueries(arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]))
