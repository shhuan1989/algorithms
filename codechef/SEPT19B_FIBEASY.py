# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/10 21:15

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List



def f(N):
    A = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2,
         7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]

    k = 1
    while 2 ** k <= N:
        k += 1

    k -= 1
    print(A[(2**k-1) % len(A)])


T = int(input())
for ti in range(T):
    N = int(input())
    f(N)