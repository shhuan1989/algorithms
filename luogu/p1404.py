# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/10/21 20:10

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


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        x = int(input())
        A.append(x * 1000)


    def check(avg):
        presum = [0]
        for v in A:
            presum.append(presum[-1] + v - avg)

        premin = [0]
        for i in range(1, N+1):
            premin.append(min(premin[-1], presum[i]))

        for right in range(N, M-1, -1):
            if presum[right] - premin[right - M] >= 0:
                return True

        return False


    lo, hi = 0, 2000 * 1000 + 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(mid):
            lo = mid + 1
        else:
            hi = mid - 1

    print(hi)