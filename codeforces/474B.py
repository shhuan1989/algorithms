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
created by shhuan at 2017/11/23 10:18

"""

N = int(input())
A = [int(x) for x in input().split()]

M = int(input())

Q = [int(x) for x in input().split()]


left = [0] * (N + 1)
for i in range(1, N+1):
    left[i] = left[i-1] + A[i-1]


for q in Q:
    m = bisect.bisect_left(left, q)
    print(m)
