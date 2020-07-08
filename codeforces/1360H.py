# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/4

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(bits, remove):
    lo, hi = 0, (1 << bits) - 1
    half = ((1 << bits) - len(remove) + 1) // 2
    while lo <= hi:
        m = (lo + hi) // 2
        # how many vals <= m
        left = m + 1 - len([v for v in remove if v <= m])
        if left == half:
            while m >= 0:
                if m not in remove:
                    return m
                m -= 1
            return m
        elif left > half:
            hi = m - 1
        else:
            lo = m + 1
    
    return 0

T = int(input())
ans = []
for i in range(T):
    N, M = map(int, input().split())
    remove = set()
    for i in range(N):
        remove.add(int(input(), 2))
    v = solve(M, remove)
    v = bin(v)[2:]
    v = '0' * (M-len(v)) + v
    ans.append(v)

print('\n'.join(ans))