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
created by shhuan at 2017/11/22 21:16

"""

N = int(input())
A = [int(x) for x in input().split()]

gift = collections.defaultdict(list)

for i, v in enumerate(A):
    gift[v].append(i+1)

t = min(len(gift[1]), len(gift[2]), len(gift[3]))

print(t)

if t > 0:
    for i in range(t):
        print(gift[1][i], gift[2][i], gift[3][i])