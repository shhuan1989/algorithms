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
created by shhuan at 2017/11/22 10:24

"""

N = int(input())
A = [int(x) for x in input().split()]

sm = collections.defaultdict(int)

for v in A:
    sm[v] += v

MA = max(A)
dp = [0] * (MA + 5)

for i in range(1, MA+1):
    dp[i] = max(dp[i-1], dp[i-2]+sm[i])
print(dp[MA])









