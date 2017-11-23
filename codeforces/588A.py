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
created by shhuan at 2017/11/22 22:34

"""

N = int(input())

A = []
P = []

for i in range(N):
    a, p = map(int, input().split())
    A.append(a)
    P.append(p)


ans = 0
minCost = float('inf')

for i in range(N):
    minCost = min(minCost, P[i])
    ans += minCost * A[i]

print(ans)