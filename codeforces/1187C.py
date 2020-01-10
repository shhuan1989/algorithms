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
created by shhuan at 2020/1/9 19:50

"""


def merge(s):
    q = []
    for l, r in s:
        if not q:
            q.append((l, r))
        else:
            if l <= q[-1][1]:
                pl, pr = q.pop()
                q.append((pl, max(r, pr)))
            else:
                q.append((l, r))
    return q


def solve(N, M, Q):
    A = [(l, r) for t, l, r in Q if t == 1]
    B = [(l, r) for t, l, r in Q if t == 0]

    A.sort()

    A = merge(A)

    for la, ra in A:
        for lb, rb in B:
            if la <= lb <= rb <= ra:
                print('NO')
                return
    d = [-1 for _ in range(N)]
    for l, r in A:
        for i in range(l+1, r + 1):
            d[i] = 0

    v = N+ 100
    # print(d)
    # print(A)
    ans = [0 for _ in range(N)]
    for i in range(N):
        v += d[i]
        ans[i] = v

    # print(ans)
    for l, r in B:
        if any([ans[i] > ans[i+1] for i in range(l, r)]):
            continue
        else:
            print('NO')
            return

    print('YES')
    print(' '.join(map(str, ans)))






# def test():
#     n = random.randint(2, 10)
#     a = []
#     for i in range(n):
#         l = random.randint(0, 100)
#         r = l + random.randint(0, 100)
#         a.append((l, r))
#     a.sort()
#     print(a)
#     print(merge(a))
#
# test()

N, M = map(int, input().split())
Q = []
for i in range(M):
    t, l, r = map(int, input().split())
    Q.append((t, l-1, r-1))

solve(N, M, Q)