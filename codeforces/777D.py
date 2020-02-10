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


def clip(word, target):
    if word <= target:
        return word
    
    lo, hi = 1, len(word)
    
    while lo <= hi:
        m = (lo + hi) // 2
        if word[:m] > target:
            hi = m - 1
        else:
            lo = m + 1
    
    return word[:hi]


def solve(N, A):
    ans = [A[-1]]
    for i in range(N-2, -1, -1):
        ans.append(clip(A[i], ans[-1]))
    
    print('\n'.join(ans[::-1]))
    sys.stdout.flush()


N = int(input())
A = []
for i in range(N):
    row = input()
    A.append(row)
    
solve(N, A)