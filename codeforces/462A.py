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
created by shhuan at 2017/11/24 22:42

"""



N = int(input())

A = []
for i in range(N):
    A.append(list(input()))


for r in range(N):
    for c in range(N):
        count = 0
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r+d[0], c+d[1]
            if 0 <= nr < N and 0 <= nc < N:
                if A[nr][nc] == 'o':
                    count += 1

        if count %2 != 0:
            print("NO")
            exit(0)
print("YES")
