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
created by shhuan at 2017/11/22 10:06

"""

N, M = map(int, input().split())

A = [int(x) for x in input().split()]

ans = 0

pre = 1
for i, v in enumerate(A):
    if v >= pre:
        ans += v-pre
    else:
        ans += N-pre+v
    pre = v

print(ans)