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
created by shhuan at 2017/11/22 22:29

"""

K = int(input())
A = [int(x) for x in input().split()]
A.sort(reverse=True)

t = 0
for i, v in enumerate(A):
    if t >= K:
        print(i)
        exit(0)
    t += v
if t >= K:
    print(len(A))
else:
    print(-1)