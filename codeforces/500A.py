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
created by shhuan at 2017/11/22 01:28

"""

N, T = map(int, input().split())

A = [0] + [int(x) for x in input().split()]


t = 1

while t < N:
    if t == T:
        print("YES")
        exit(0)
    elif t > T:
        print("NO")
        exit(0)

    t += A[t]

print("NO")