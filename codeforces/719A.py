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
created by shhuan at 2017/11/23 21:58

"""


MOON = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

N = int(input())

A = [int(x) for x in input().split()]

ans = 0
for start in range(len(MOON)):
    f = True
    for i in range(N):
        if MOON[(start+i) % len(MOON)] != A[i]:
            f = False
            break
    if f:
        m = MOON[(start+N) % len(MOON)]
        if m > A[-1]:
            if ans == -1:
                print(-1)
                exit(0)
            ans = 1
        elif m < A[-1]:
            if ans == 1:
                print(-1)
                exit(0)
            ans = -1

if ans == 0:
    print(-1)
elif ans == 1:
    print("UP")
else:
    print("DOWN")

