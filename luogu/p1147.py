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
created by shhuan at 2020/7/17 21:25

"""


def f(a, x, t):
    return x**2 + (2*a-1)*x - 2*t


def find(a, N):
    lo, hi = 0, 2 * 10**6 + 10

    while abs(lo - hi) > 0.1:
        d = (hi - lo) / 3
        l, r = lo + d, lo + 2 * d

        vlo, vl, vr, vhi = f(a, lo, N), f(a, l, N), f(a, r, N), f(a, hi, N)
        if vl * vr < 0:
            lo, hi = l, r
        elif vlo * vr > 0:
            lo = r
        else:
            hi = l
    lo = int(round(lo))
    return lo + a - 1 if f(a, lo, N) == 0 else -1


def solve(N):
    ans = []
    for a in range(1, N//2+1):
        b = find(a, N)
        if b > a:
            ans.append('{} {}'.format(a, b))

    return ans


def solve2(N):
    ans = []
    N *= 2
    for a in range(int(math.sqrt(N)), 1, -1):
        if N % a == 0:
            b = N // a
            if (a + b) % 2 == 1:
                ans.append('{} {}'.format((b-a+1)//2, (b+a-1)//2))
    return ans

if __name__ == '__main__':
    N = int(input())

    print('\n'.join(solve2(N)))