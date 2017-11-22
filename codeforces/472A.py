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
created by shhuan at 2017/11/22 00:30

"""

N = int(input())

primes = [1] * (N+1)

for i in range(2, N+1):
    if primes[i]:
        v = i*2
        while v <= N:
            primes[v] = 0
            v += i


for i in range(N+1):
    if not primes[i] and not primes[N-i]:
        print(i, N-i)
        exit(0)