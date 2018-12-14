# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/10 21:06

"""


N, C = map(int, input().split())
coins = 1000
lo, hi = 1, N

while lo < hi:
    h = hi - lo
    if h <= coins - C:
        break
    m = lo + h // (min(2**(max(coins//C-1, 1)), h))
    print('1 {}'.format(m))
    coins -= 1
    sys.stdout.flush()
    status = int(input())
    if status == 1:
        print('2')
        sys.stdout.flush()
        coins -= C
        hi = m
    else:
        lo = m + 1

while lo < hi:
    print('1 {}'.format(lo))
    coins -= 1
    sys.stdout.flush()
    status = int(input())
    if status == 1:
        hi = lo
        print('2')
        coins -= C
        sys.stdout.flush()
        break
    lo += 1


print('3 {}'.format(hi))
sys.stdout.flush()
