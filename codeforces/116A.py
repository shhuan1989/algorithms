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
created by shhuan at 2017/11/21 22:32

"""

N = int(input())

A = [0] * N
B = [0] * N
for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b


ans = 0

t = 0
for i in range(N):
    t = max(0, t-A[i])
    t += B[i]
    ans = max(ans, t)

print(ans)