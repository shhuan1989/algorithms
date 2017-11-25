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
created by shhuan at 2017/11/24 21:10

"""

N = int(input())

A = [0] * (N+1)

for i in range(1, N+1):
    p = int(input())
    A[i] = p

ans = 0

for i in range(1, N+1):
    l = 1
    u = A[i]
    while u > 0:
        u = A[u]
        l += 1
    ans = max(ans, l)

print(ans)
