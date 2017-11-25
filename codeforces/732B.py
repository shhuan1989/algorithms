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
created by shhuan at 2017/11/23 22:24

"""


N, K = map(int, input().split())


A = [int(x) for x in input().split()]

t = sum(A)
for i in range(1, N):
    A[i] = max(A[i], K-A[i-1])

print(sum(A) - t)
print(" ".join(map(str, A)))



