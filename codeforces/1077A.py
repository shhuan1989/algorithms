# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/11/16 22:37

"""

T = int(input())

for ti in range(T):
    a, b, k = map(int, input().split())

    x = k // 2
    if k % 2 == 0:
        print(a * x - b * x)
    else:
        print(a*x+a-b*x)