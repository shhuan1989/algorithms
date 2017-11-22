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
created by shhuan at 2017/11/21 23:37

"""

N = int(input())

A = [int(x) for x in input().split()]


ans = 0
p = float('-inf')

c = 0
for v in A:
    if v >= p:
        c += 1
    else:
        ans = max(ans, c)
        c = 1
    p = v
ans = max(ans, c)
print(ans)
