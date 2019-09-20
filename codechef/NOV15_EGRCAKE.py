# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/10 20:22

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List



def f(n, k):

    A = [i for i in range(n)]
    A = A[k:] + A[:k]
    B = [0] * n

    B[0] = True

    i = 0
    while True:
        i = A[i]
        if B[i]:
            break
        B[i] = 1

    c = sum(B)
    if c == n:
        print('Yes')
    else:
        print('No {}'.format(n-c))


T = int(input())
for ti in range(T):
    n, k = map(int, input().split())
    f(n, k)