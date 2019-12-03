# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2019/12/1 14:50

"""


def check_pt(P, T, cost):
    if not T:
        return cost > 0

    if cost < T[-1]:
        return False

    for i, p in enumerate(P):
        ncost = min(cost-p, T[-1]-1)
        if len(T) > 1 and ncost <= T[-2]:
            continue
        if check_pt(P[:i] + P[i+1:], T[:-1], ncost):
            return True

    return False


def check(Q, P, T, cost):
    if not Q and not P:
        return cost >= 1

    if not P:
        return cost >= sum(Q)

    if not Q:
        return check_pt(P, T, cost)

    t = T[-1] + 1
    tq = 0
    for qi in range(len(Q)-1, -1, -1):
        tq += Q[qi]
        if t + tq - 1 > cost:
            return False

        tr = cost-tq
        for pi in range(len(P)):
            p = P[pi]
            ncost = min(tr-p, T[-1]-1)
            if len(T) <= 1 or ncost > T[-2]:
                if check(Q[:qi], P[:pi]+P[pi+1:], T[:-1], ncost):
                    return True
    return False


def solve(Q, P, T):
    lo, hi = T[-1], T[-1] + max(Q) + max(P) + 1

    while lo <= hi:
        m = (lo + hi) // 2
        if check(Q, P, T, m):
            hi = m - 1
        else:
            lo = m + 1

    return lo


T = int(input())
for ti in range(T):
    N, M = map(int, input().split())
    Q = [int(x) for x in input().split()]
    P = [int(x) for x in input().split()]
    T = [int(x) for x in input().split()]

    print(solve(Q, P, T))