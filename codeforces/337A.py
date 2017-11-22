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
created by shhuan at 2017/11/21 23:21

"""

N, M = map(int, input().split())

F = [int(x) for x in input().split()]

F.sort()

d = M - N
ans = float('inf')
for left in range(d+1):
    right = d - left
    ans = min(ans, F[M-right-1] - F[left])

print(ans)