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
created by shhuan at 2017/11/22 00:22

"""


N = int(input())

A = [0] * (N+1)

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

for v in a[1:]:
    A[v] = 1
for v in b[1:]:
    A[v] = 1

if sum(A) == N:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")