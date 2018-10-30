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
created by shhuan at 2018/10/18 23:50

"""

def solve(N, V1, V2, steps):
    v = V1
    spy = True
    r, c = 0, 0
    for s in steps:
        if s == '*':
            spy = not spy
            v = V1 if spy else V2
        else:
            if s == 'N':
                r -= v
            elif s == 'S':
                r += v
            elif s == 'W':
                c -= v
            else:
                c += v

    d = max(abs(r), abs(c))
    if d % 2 == 0:
        return 'B'
    else:
        return 'W'





T = int(input())
for i in range(T):
    N, V1, V2 = map(int, input().split())
    S = input()
    print(solve(N, V1, V2, S))
