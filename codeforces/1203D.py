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
created by shhuan at 2020/1/9 21:29

"""


def solve(S, T):
    N, M = len(S), len(T)
    left = [-1 for _ in range(N)]

    si, ti = 0, 0
    while si < N:
        if ti >= M:
            left[si] = left[si-1]
            si += 1
            continue
        if S[si] == T[ti]:
            left[si] = ti
            ti += 1
        else:
            left[si] = left[si-1] if si > 0 else -1
        si += 1

    right = [M for _ in range(N)]
    si, ti = N-1, M-1
    while si >= 0:
        if ti < 0:
            right[si] = right[si+1]
            si -= 1
            continue

        if S[si] == T[ti]:
            right[si] = ti
            ti -= 1
        else:
            right[si] = right[si+1] if si+1 < N else M
        si -= 1

    ans = 0
    for i in range(N):
        if left[i] >= M-1:
            ans = max(ans, N-i-1)
            break
        j = bisect.bisect_right(right, left[i] + 1)
        ans = max(ans, j-i-(2 if left[i] >= 0 else 1))
    print(ans)


S = input()
T = input()
solve(S, T)