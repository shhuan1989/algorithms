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
created by shhuan at 2017/11/24 23:54

"""

N, K = map(int, input().split())

ans = float('-inf')

for i in range(N):
    f, t = map(int, input().split())

    if t > K:
        ans = max(ans, f-(t-K))
    else:
        ans = max(ans, f)

print(ans)