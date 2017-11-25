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
created by shhuan at 2017/11/23 23:12

"""

N = int(input())

def check(v):
    b = bin(v)[2:]
    if len(b) % 2 == 0:
        return False

    h = len(b) // 2
    if b == '1' * (h+1) + '0' * h:
        return True

    return False




if check(N):
    print(N)
    exit(0)

for v in range(N//2, 0, -1):
    if N % v == 0:
        if check(v):
            print(v)
            exit(0)
print(1)