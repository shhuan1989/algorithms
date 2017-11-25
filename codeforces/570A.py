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
created by shhuan at 2017/11/24 21:26

"""

N, M = map(int, input().split())


wins = collections.defaultdict(int)
for i in range(M):
    a = [int(x) for x in input().split()]

    maxa = -1
    w = -1
    for j in range(N):
        if a[j] > maxa:
            maxa = a[j]
            w = j+1

    wins[w] += 1

maxa = -1
ans = -1
for i in sorted(wins.keys()):
    if wins[i] > maxa:
        maxa = wins[i]
        ans = i

print(ans)


