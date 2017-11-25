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
created by shhuan at 2017/11/24 20:05

"""


N = int(input())

A = [int(x) for x in input().split()]

A.sort()

t = 2
ans = 0
for v in A:
    ans += t*v
    t += 1
ans -= A[-1]

print(ans)
