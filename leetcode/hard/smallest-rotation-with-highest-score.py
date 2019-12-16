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
created by shhuan at 2019/12/12 23:17

"""

class Solution:
    def bestRotation(self, A: List[int]) -> int:
        """
        每个数字的一分的移动次数在两个区间中。
        计算所有的区间，然后找到重合度最高的点
        :param A:
        :return:
        """
        N = len(A)
        add = [0] * N
        minus = [0] * (N+1)
        for i, v in enumerate(A):
            if i-v >= 0:
                add[0] += 1
                minus[i-v+1] += 1
            if min(N+i-v, N-1) >= i+1:
                add[i+1] += 1
                minus[min(N+i-v+1, N)] += 1

        score, K = 0, 0
        count = 0
        for i in range(N):
            count -= minus[i]
            count += add[i]
            if count > score:
                score = count
                K = i

        return K

s = Solution()
print(s.bestRotation([2, 3, 1, 4, 0]))
print(s.bestRotation([1, 3, 0, 2, 4]))
