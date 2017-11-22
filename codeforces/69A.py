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
created by shhuan at 2017/11/21 23:07

"""

N = int(input())

X, Y, Z = 0, 0, 0
for i in range(N):
    x, y, z = map(int, input().split())
    X += x
    Y += y
    Z += z

if X == 0 and Y == 0 and Z == 0:
    print("YES")
else:
    print("NO")