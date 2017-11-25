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
created by shhuan at 2017/11/24 17:10

"""

# N, M = map(int, input().split())
#
# A = [int(x) for x in input().split()]

N, M = 10**5, 10**5
A = [random.randint(1, 10**5) for _ in range(N)]
t0 = time.time()

right = [0] * (N+1)
nums = set()
for i in range(N-1, -1, -1):
    nums.add(A[i])
    right[i] = len(nums)

for i in range(M):
    l = random.randint(1, N)
    # l = int(input())
    print(right[l-1])

print(time.time() - t0)