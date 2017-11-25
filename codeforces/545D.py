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
created by shhuan at 2017/11/24 21:33

"""

N = int(input())

A = [int(x) for x in input().split()]

A.sort()
ans = 0

total = 0
for i, v in enumerate(A):
    if total <= v:
        ans += 1
        total += v

print(ans)