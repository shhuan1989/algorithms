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
created by shhuan at 2017/11/8 08:35

"""

N, T = map(int, input().split())

A = [int(x) for x in input().split()]


for i in range(N):
    T -= 86400 - A[i]
    if T <= 0:
        print(i+1)
        exit(0)

print(N)