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
created by shhuan at 2017/11/21 22:57

"""

N = int(input())

P = [0] * N
Q = [0] * N
for i in range(N):
    p, q = map(int, input().split())

    P[i] = p
    Q[i] = q

ans = 0
for i in range(N):
    if Q[i] - P[i] >= 2:
        ans += 1

print(ans)