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
created by shhuan at 2017/11/24 18:24

"""

A = [int(x) for x in input().split()]

wc = collections.Counter(A)

leg = [k for k, v in wc.items() if v >= 4]

if not leg:
    print("Alien")
    exit(0)

leg = leg[0]

other = []

c = 0
for v in A:
    if v == leg and c < 4:
        c += 1
    else:
        other.append(v)

if other[0] == other[1]:
    print("Elephant")
else:
    print("Bear")


