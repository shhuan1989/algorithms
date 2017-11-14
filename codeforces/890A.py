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
created by shhuan at 2017/11/12 23:56

"""

A = [int(x) for x in input().split()]


idx = [i for i in range(6)]

total = sum(A)
if total % 2 != 0:
    print('NO')
    exit(0)
for i in itertools.combinations(idx, 3):
    # print(i)
    half = sum([A[j] for j in i])
    if half == total // 2:
        print('YES')
        exit(0)
print('NO')