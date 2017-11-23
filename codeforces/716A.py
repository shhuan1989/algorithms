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
created by shhuan at 2017/11/22 23:14

"""

N, C = map(int, input().split())

A = [int(x) for x in input().split()]

ans = 1
p = A[0]

for t in A[1:]:
    if t-p > C:
        ans = 1
    else:
        ans += 1
    p = t

print(ans)
