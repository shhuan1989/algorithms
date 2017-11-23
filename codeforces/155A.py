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
created by shhuan at 2017/11/22 11:27

"""

N = int(input())

A = [int(x) for x in input().split()]

maxa = A[0]
mina = A[0]
ans = 0


for v in A[1:]:
    if v > maxa or v < mina:
        ans += 1

    maxa = max(maxa, v)
    mina = min(mina, v)

print(ans)