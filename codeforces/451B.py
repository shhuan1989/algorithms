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
created by shhuan at 2017/11/24 13:49

"""

N = int(input())

A = [int(x) for x in input().split()]

B = list(sorted((A)))


l = 0
r = N-1

while l < N and A[l] == B[l]:
    l += 1
while r >= 0 and A[r] == B[r]:
    r -=1

if l < r:
    if A[l:r+1] == list(reversed(B[l:r+1])):
        print("yes")
        print(l+1, r+1)
    else:
        print("no")
else:
    print("yes")
    print(1, 1)