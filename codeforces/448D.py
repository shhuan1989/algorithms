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


# count of nums  less than or equal to val
# return True if count < K
import math

def check(val, N, M,  K):
    count = val//M * M
    count += sum([val//a for a in range(max(1, val // M + 1), min(val // 2, N)+1)])
    count += max(min(val, N) - val//2, 0)
    
    return count < K


def solve(N, M, K):
    N, M = list(sorted([N, M]))
    lo, hi = int(K/sum(1/i for i in range(1, N+1))), K
    while lo <= hi:
        m = (lo + hi) // 2
        # print(m)
        if check(m, N, M, K):
            lo = m + 1
        else:
            hi = m - 1
    
    return lo
        

N, M, K = map(int, input().split())
print(solve(N, M, K))