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
created by shhuan at 2018/10/18 20:58

"""

from collections import deque


def digitsum(val):
    res = 0
    while val > 0:
        res += val % 10
        val //= 10

    return res


def stepToTarget(n, d, target):
    q = deque([(n, 0)])
    visited = {n}
    maxStep = 1000
    while q:
        v, s = q.popleft()
        if v == target:
            return s

        for u in [v+d, digitsum(v)]:
            if u not in visited:
                visited.add(u)
                q.append((u, s+1))
        if s > maxStep:
            return -1

    return -1


def solve(n, d):
    for target in range(10):
        step = stepToTarget(n, d, target)
        if step >= 0:
            return ' '.join(map(str, [target, step]))




T = int(input())
for ti in range(T):
    N, D = map(int, input().split())
    print(solve(N, D))