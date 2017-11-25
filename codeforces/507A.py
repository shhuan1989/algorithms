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
created by shhuan at 2017/11/24 13:10

"""

N, K = map(int, input().split())

A = [int(x) for x in input().split()]

A = [(v, i+1) for i, v in enumerate(A)]
A.sort()

total = 0
i = 0
while i < N and total <= K:
    total += A[i][0]
    i += 1

if total > K:
    print(i-1)
    print(" ".join(map(str, [x[1] for x in A[:i-1]])))
else:
    print(i)
    print(" ".join(map(str, [x[1] for x in A[:i]])))