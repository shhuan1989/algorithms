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
created by shhuan at 2017/11/21 23:32

"""

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

dm = [0] * (d+1)

for i in range(1, d+1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
        dm[i] = 1

print(sum(dm))