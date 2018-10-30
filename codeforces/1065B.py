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
created by shhuan at 2018/10/19 22:56

"""


# N个顶点最多N*(N-1)//2条边
# M条边最多使得2*M个顶点不是孤立点

N, M = map(int, input().split())

if M == 0 or N == 1:
    print(N, N)
else:

    n = 1
    while n*(n-1) < 2*M:
        n += 1

    vmax = max(N-n, 0)
    vmin = max(N-2*M, 0)

    print(vmin, vmax)

