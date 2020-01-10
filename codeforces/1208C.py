# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/1/8 22:25

divide the grid into 4 quadrants

1 | 2
-----
3 | 4

"""


N = int(input())
A = [[0 for _ in range(N)] for _ in range(N)]
v = 0
for i in range(N//2):
    for j in range(N//2):
        A[i][j] = 4 * v + 1
        A[i][j + N // 2] = 4 * v + 2
        A[i + N // 2][j] = 4 * v + 3
        A[i + N // 2][j + N // 2] = 4 * v
        v += 1

for row in A:
    print(' '.join(map(str, row)))