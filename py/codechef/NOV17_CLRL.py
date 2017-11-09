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
created by shhuan at 2017/11/8 22:13

"""

T = int(input())

for ti in range(T):
    N, R = map(int, input().split())

    A = [int(x) for x in input().split()]
    l = float('-inf')
    r = float('inf')

    ans = True
    for v in A:
        if v <= l or v >= r:
            ans = False
            break
        if v < R:
            l = v
        elif v > R:
            r = v
    if ans:
        print('YES')
    else:
        print('NO')
