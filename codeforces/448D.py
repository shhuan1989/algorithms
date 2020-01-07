
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
created by shhuan at 2019/12/28 10:37

"""

# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/27/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


# count of nums  less than or equal to val
# return True if count < K
def check(val):
    if N == 1:
        return min(M, val) < K
    if M == 1:
        return min(N, val) < K
    if N > val // 2:
        return val // M * M + (min(N, val)-val//2) + sum([val // a for a in range(max(1, val // M + 1), val//2 + 1)]) < K
    else:
        return val // M * M + sum([val // a for a in range(max(1, val // M + 1), min(N, val) + 1)]) < K
    # count = 0
    # a = 1
    # while a <= N:
    #     b = min(M, val // a)
    #     if b == 1:
    #         count += min(val, N) - a + 1
    #         break
    #     elif b < M:
    #         count += sum([val//i for i in range(a, N+1)])
    #         break
    #     al, ar = a, N
    #     while al <= ar:
    #         am = (al + ar) // 2
    #         if min(M, val//am) >= b:
    #             al = am + 1
    #         else:
    #             ar = am - 1
    #     na = al
    #     count += (na-a)*b
    #     a = na
    #
    # return count < K


def solve():
    lo, hi = 1, N * M
    while lo <= hi:
        m = (lo + hi) // 2
        if check(m):
            lo = m + 1
        else:
            hi = m - 1

    return lo


# N, M, K = map(int, input().split())
N, M, K = 500000, 500000, 1
t0 = time.time()
print(solve())
print(time.time() - t0)