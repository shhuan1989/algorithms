# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/11/24 15:28

"""

N, K = map(int, input().split())

r = 2 * N // K
g = 5 * N // K
b = 8 * N // K

if r * K < 2*N:
    r += 1

if g * K < 5*N:
    g += 1

if b * K < 8 * N:
    b += 1

print(r+g+b)