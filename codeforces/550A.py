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
created by shhuan at 2017/11/23 20:21

"""

S = input()

N = len(S)

if N <= 3:
    print("NO")
    exit(0)


maxab, minab, maxba, minba = -1, N, -1, N

for i in range(N):
    if S[i:i+2] == "AB":
        maxab = max(maxab, i)
        minab = min(minab, i)
    if S[i: i+2] == "BA":
        maxba = max(maxba, i)
        minba = min(minba, i)


for a in [maxab, minab]:
    for b in [minba, maxba]:
        if 0 <= a < N and 0 <= b < N and abs(a-b) > 1:
            print("YES")
            exit(0)

print("NO")


