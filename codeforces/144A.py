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
created by shhuan at 2017/11/22 00:14

"""

N = int(input())
A = [int(x) for x in input().split()]

mina = min(A)
maxa = max(A)

mini = -1
maxi = -1
for i in range(N-1, -1, -1):
    if A[i] == mina:
        mini = i
        break

for i in range(N):
    if A[i] == maxa:
        maxi = i
        break

if mini > maxi:
    print(N-1-mini+maxi)
else:
    print(N-2-mini+maxi)




