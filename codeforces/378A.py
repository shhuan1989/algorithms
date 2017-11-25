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
created by shhuan at 2017/11/24 22:14

"""

a, b = map(int, input().split())

w, d, l = 0, 0, 0

for i in range(1, 7):
    if abs(a-i) == abs(b-i):
        d += 1
    elif abs(a-i) < abs(b-i):
        w += 1
    else:
        l += 1

print(w, d, l)