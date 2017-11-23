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
created by shhuan at 2017/11/22 22:44

"""



N = int(input())

A = [int(x) for x in input().split()]

MAXN = int(math.sqrt(max(A)+1))+5
# MAXN = 10**6+5

primes = [1] * MAXN

for i in range(2, MAXN):
    if primes[i]:
        v = i * 2
        while v < MAXN:
            primes[v] = 0
            v += i
primes[1] = 0
# primes = {i for i in range(2, MAXN) if primes[i]}
#
# print(list(sorted(primes)))


for v in A:
    u = int(math.sqrt(v))
    if primes[u] and u**2 == v:
        print("YES")
    else:
        print("NO")

