# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2019/2/13 20:08

"""


def gcd(x, y):
    while y:
        x, y = y, x%y

    return x


def solve(ang):
    g = gcd(ang, 180)
    k = ang // g
    n = 180 // g

    if k + 1 == n:
        k *= 2
        n *= 2

    return n

T = int(input())
for ti in range(T):
    ang = int(input())
    print(solve(ang))