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
created by shhuan at 2017/11/24 20:22

"""

N, K = map(int, input().split())
A = [int(x) for x in input().split()]

height = sum(A[:K])
minHeigh  = height
ans = 1

for i in range(K, N):
    height += A[i]
    height -= A[i-K]
    if height < minHeigh:
        minHeigh = height
        ans = i-K+2

print(ans)