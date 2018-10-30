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
created by shhuan at 2018/10/18 20:40

"""


T = int(input())

for i in range(T):
    N = int(input())

    n = 2 ** (N // 26) if N % 26 != 0 else 2 ** (N // 26 - 1)

    t = N % 26
    if 0 < t <= 2:
        print(' '.join(map(str, [n, 0, 0])))
    elif 2 < t <= 10:
        print(' '.join(map(str, [0, n, 0])))
    else:
        print(' '.join(map(str, [0, 0, n])))
