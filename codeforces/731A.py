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
created by shhuan at 2017/11/23 22:08

"""


A = [chr(ord('a') + i) for i in range(26)]


def step(pos, t):
    a = 0
    i = pos
    while A[i] != t:
        i = (i+1) % 26
        a += 1

    b = 0
    i = pos
    while A[i] != t:
        i = (i-1+26) % 26
        b += 1

    return min(a, b)



S = input()

ans = 0
pos = 0
for v in S:
    ans += step(pos, v)
    pos = A.index(v)

print(ans)

