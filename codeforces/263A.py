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
created by shhuan at 2017/11/21 22:41

"""

A = []

for r in range(5):
    A.append([int(x) for x in input().split()])


row, col = -1, -1
for r in range(5):
    for c in range(5):
        if A[r][c] == 1:
            row = r + 1
            col = c + 1


ans = abs(row-3) + abs(col-3)

print(ans)