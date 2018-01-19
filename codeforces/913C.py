# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/11/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


N, L = map(int, input().split())
C = [int(x) for x in input().split()]


for i in range(1, N):
  C[i] = min(C[i], 2 * C[i-1])

bestans = 2*10**18
exactans = 0
for i in range(N-1, -1, -1):
  here = L // (1 << i)
  exactans += here * C[i]
  L -= here * (1 << i)
  bestans = min(bestans, exactans+C[i])

print(min(bestans, exactans))
