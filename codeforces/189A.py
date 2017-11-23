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
created by shhuan at 2017/11/22 11:39

"""

n, a, b, c = map(int, input().split())


dp = [0] * (n+1)

for v in [a, b, c]:
    if v <= n:
        dp[v] = 1

for i in range(n+1):
    if dp[i] == 0:
        continue

    for v in [a, b, c]:
        if i + v <= n:
            dp[i+v] = max(dp[i+v], dp[i]+1)

print(dp[n])