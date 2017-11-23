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
created by shhuan at 2017/11/22 11:36

"""


N, K = map(int, input().split())

t = 4*60-K

# 5, 10, 15, 5 * n
# (5+5n)n//2 <= t
# 5(n+1)n <= 2t

for i in range(1, N+1):
    if 5*(i+1)*i > 2*t:
        print(i-1)
        exit(0)
print(N)
