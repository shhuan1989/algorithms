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
created by shhuan at 2017/11/22 00:37

"""

N = int(input())
A = []

for i in range(N):
    A.append(input())


ans = 1
p = A[0]
for v in A[1:]:
    if v != p:
        ans += 1
        p = v
print(ans)