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
created by shhuan at 2017/11/24 19:56

"""

n, m, z = map(int, input().split())

a = [0] * (z+1)

x = n
while x <= z:
    a[x] = 1
    x += n

y = m
while y <= z:
    a[y] += 1
    y += m

print(len([x for x in a if x == 2]))