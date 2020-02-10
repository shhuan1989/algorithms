# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/17/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

from functools import lru_cache

N, D = map(int, input().split())
A = []
for i in range(N):
    v = int(input())
    A.append(v)

MAXN = max(A)
gems = [0 for _ in range(MAXN+1)]
for v in A:
    gems[v] += 1


@lru_cache(maxsize=None)
def solve(i, j):
    if i > MAXN or j <= 0:
        return 0
    
    # print(i,j,gems[i] + max(solve(i + j - 1, j - 1), solve(i + j, j), solve(i + j + 1, j + 1)))
    return gems[i] + max(solve(i + j - 1, j - 1), solve(i + j, j), solve(i + j + 1, j + 1))
    
print(solve(D, D))