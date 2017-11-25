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
created by shhuan at 2017/11/24 21:55

"""


T = int(input())

for i in range(T):
    n = int(input())

    total = n*(n+1)//2

    i = 0
    while 2**i <= n:
        total -= 2**(i+1)
        i += 1

    print(total)

