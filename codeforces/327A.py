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
created by shhuan at 2017/11/22 13:04

"""


N = int(input())
A = [int(x) for x in input().split()]

ans = 0
for i in range(N):
    for j in range(i+1, N+1):

        d = j-i - sum(A[i:j] or [0])
        ans = max(ans, sum(A[:i] or [0]) + d + sum(A[j:] or [0]))

print(ans)