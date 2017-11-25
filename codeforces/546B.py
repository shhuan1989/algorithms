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
created by shhuan at 2017/11/24 21:50

"""

N = int(input())

A = [int(x) for x in input().split()]

V = [0] * (N*2+1)

ans = 0
for v in sorted(A):
    if V[v] == 0:
        V[v] = 1
    else:
        for i in range(v+1, N*2+1):
            if V[i] == 0:
                V[i] = 1
                ans += i-v
                break
print(ans)

