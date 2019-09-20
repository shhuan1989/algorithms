# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/3 23:44

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
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        N, M = len(A), len(B)
        ai, bi = 0, 0
        while ai < N and bi < M:
            a, b= A[ai], B[bi]
            if a[1] < b[0]:
                ai += 1
            elif b[1] < a[0]:
                bi += 1
            elif a[0] <= b[0] <= b[1] <= a[1]:
                ans.append([b[0], b[1]])
                bi += 1
            elif b[0] <= a[0] <= a[1] <= b[1]:
                ans.append([a[0], a[1]])
                ai += 1
            elif a[0] <= b[0] <= a[1] <= b[1]:
                ans.append([b[0], a[1]])
                ai += 1
            else:
                ans.append([a[0], b[1]])
                bi += 1
        return ans


s = Solution()
print(s.intervalIntersection(A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]))