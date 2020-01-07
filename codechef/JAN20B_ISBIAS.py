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
created by shhuan at 2020/1/4 15:25

"""


# def count(seq, l, r):
#     slen = 0
#     for i in range(len(seq)):
#         a, b, c, d = seq[i][0], seq[i][1], l, r
#         if c <= a < d or a <= c < d <= b or c < b <= d or c <= a < b <= d:
#             slen += 1
#     return slen

def check(a, b, c, d):
    return c <= a < d or a <= c < d <= b or c < b <= d or c <= a < b <= d


def count(seq, l, r):
    ul = bisect.bisect_left(seq, [l, -1])
    ur = bisect.bisect_right(seq, [r, N])
    slen = 0
    if ur - ul >= 3:
        slen = ur - ul - 2
        for i in [ul-1, ul, ur-1, ur]:
            if 0 <= i < len(seq) and check(seq[i][0], seq[i][1], l, r):
                slen += 1
    elif ur - ul >= 0:
        for i in range(max(0, ul - 1), min(ur + 1, len(seq))):
            if check(seq[i][0], seq[i][1], l, r):
                slen += 1
    return slen


def solve(N, A, Q, queries):
    up = [[0, 0]]
    down = [[0, 0]]
    for i, v in enumerate(A):
        if v > A[up[-1][1]]:
            up[-1][1] = i
        else:
            if up[-1][0] == up[-1][1]:
                up.pop()
            up.append([i, i])

        if v < A[down[-1][1]]:
            down[-1][1] = i
        else:
            if down[-1][0] == down[-1][-1]:
                down.pop()
            down.append([i, i])
    if up[-1][0] == up[-1][1]:
        up.pop()
    if down[-1][0] == down[-1][1]:
        down.pop()

    ans = []
    for l, r in queries:
        uplen, downlen = count(up, l, r), count(down, l, r)
        ans.append('YES' if uplen == downlen else 'NO')

    print('\n'.join(ans))


N, Q = map(int, input().split())
A = [int(x) for x in input().split()]
queries = []
for i in range(Q):
    l, r = map(int, input().split())
    queries.append((l-1, r-1))
solve(N, A, Q, queries)