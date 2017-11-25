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
created by shhuan at 2017/11/24 18:37

"""

N, K = map(int, input().split())

A = [int(x) for x in input().split()]


total = 0
for i, v in enumerate(A):
    total += v
    d = min(total, 8)
    total -= d
    K -=d

    if K <= 0:
        print(i+1)
        exit(0)

print(-1)
