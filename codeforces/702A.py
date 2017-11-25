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
created by shhuan at 2017/11/24 22:00

"""


N = int(input())

A = [int(x) for x in input().split()]


ans = 0
p = float('inf')
pi = -1

for i, v in enumerate(A):
    if v <= p:
        ans = max(ans, i-pi)
        pi = i
    p = v
ans = max(ans, N - pi)

print(ans)
