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
created by shhuan at 2017/11/9 23:05

"""

N = int(input())
A = [int(x) for x in input().split()]


ans = 0
for i in range(1, N-1):
    if A[i-1] < A[i] > A[i+1] or A[i-1] > A[i] < A[i+1]:
        ans += 1

print(ans)