# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/30/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

N = int(input())
A = [int(x) for x in input().split()]

t = sum(A)
ans = t
for gap in range(2, N // 2):
    if N % gap != 0 or N - N // gap < 3:
        continue
    for s in range(gap):
        c = sum([A[(s+i) % N] for i in range(0, N, gap)])
        # print(gap, s, c, [(s+i) % N for i in range(1, N, gap)])
        ans = max(ans, c)

print(ans)