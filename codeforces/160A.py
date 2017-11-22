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
created by shhuan at 2017/11/21 22:44

"""

N = int(input())

A = [int(x) for x in input().split()]

total = sum(A)

A.sort(reverse=True)

t = 0
for i in range(N):
    t += A[i]
    if t * 2 > total:
        print(i+1)
        exit(0)