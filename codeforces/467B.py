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
created by shhuan at 2017/11/22 23:05

"""

N, M, K = map(int, input().split())

A = []
for i in range(M+1):
    A.append(int(input()))


ans = 0
for i in range(M):
    v = A[i] ^ A[M]

    k = 0
    while v > 0:
        if v & 1:
            k += 1
        v >>= 1

    if k <= K:
       ans += 1


print(ans)

