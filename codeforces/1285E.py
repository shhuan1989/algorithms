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
created by shhuan at 2020/1/10 23:44

"""


def solve(N, A):
    L = [l for l, r in A]
    R = [r for l, r in A]
    L.sort()
    R.sort()

    LR = [(l, 1) for l, r in A] + [(r, -1) for l, r in A]
    LR.sort()

    s = 0
    neck = []
    count = 0
    for i, (l, v) in enumerate(LR):
        s += v
        if s == 1:
            neck.append((l, LR[i+1][0] if i + 1 < len(LR) else float('inf')))
        elif s == 0:
            count += 1
    if s != 0:
        count += 1

    if not neck:
        return count

    ans = 0
    for l, r in A:
        i = bisect.bisect_right(neck, (l-1, float('inf')))
        j = bisect.bisect_right(neck, (r, float('inf')))
        if i >= j:
            continue
        if neck[i][0] == l and neck[j-1][1] == r:
            ans = max(ans, count - 1)
        else:
            ans = max(ans, count + j - i - 1)

    return ans


T = int(input())
ans = []
for ti in range(T):
    N = int(input())
    A = []
    for ni in range(N):
        l, r = map(int, input().split())
        A.append((l, r))
    ans.append(solve(N, A))

print('\n'.join(map(str, ans)))