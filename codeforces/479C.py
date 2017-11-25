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
created by shhuan at 2017/11/24 20:49

"""

N = int(input())
A = []

for i in range(N):
    a, b = map(int, input().split())
    A.append((a, b))


A.sort()

ans = 0
for i in range(N):
    if A[i][1] < ans:
        ans = A[i][0]
    ans = max(ans, A[i][1])

print(ans)