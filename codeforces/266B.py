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
created by shhuan at 2017/11/21 23:13

"""

N, T = map(int, input().split())

S = list(input())


for i in range(T):
    t = [''] * N
    j = 0
    while j < N:
        if j < N-1 and S[j] == 'B' and S[j+1] == 'G':
            t[j] = 'G'
            t[j+1] = 'B'
            j += 2
        else:
            t[j] = S[j]
            j += 1
    S = t

print("".join(S))
