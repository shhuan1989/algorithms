# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/25/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


MAXN = 3001
mark = [True for _ in range(MAXN)]
mark[0] = mark[1] = False
for i in range(2, MAXN):
    if mark[i]:
        v = i + i
        while v < MAXN:
            mark[v] = False
            v += i

primes = [i for i in range(MAXN) if mark[i]]


def check(val):
    factors = 0
    for v in primes:
        if factors > 2:
            break
        if v > val:
            break
        if val % v == 0:
            factors += 1
            while val % v == 0:
                val //= v
    if val > 1:
        factors += 1
    
    return factors == 2

N = int(input())
print(sum([1 for i in range(1, N+1) if check(i)]))

