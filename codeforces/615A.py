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
created by shhuan at 2017/11/24 13:38

"""

N, M = map(int, input().split())

on = [0] * (M+1)

for i in range(N):
    b = [int(x) for x in input().split()]
    for v in b[1:]:
        on[v] = 1

if sum(on) == M:
    print("YES")
else:
    print("NO")