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
created by shhuan at 2017/11/17 22:54

"""

N = int(input())
A = [int(x) for x in input().split()]
#
# N = 2000
# A = [random.randint(2, 5) for _ in range(N)]
#
# t0 = time.time()

def gcd(x, y):
    if x < y:
        x, y = y, x

    if y == 0:
        return x

    return gcd(x%y, y)

if any([v == 1 for v in A]):
    print(len([v for v in A if v != 1]))
else:

    d = float('inf')

    for i in range(N):
        v = A[i]
        for j in range(i+1, min(N, i+d+1)):
            v = gcd(v, A[j])
            if v == 1:
                d = min(d, j-i)

    if d != float('inf'):
        print(d + N - 1)
    else:
        print(-1)

    # print(time.time() - t0)


