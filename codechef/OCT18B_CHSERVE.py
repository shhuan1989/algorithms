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
created by shhuan at 2018/10/18 20:29

"""

T = int(input())

for ti in range(T):
    p1, p2, k = map(int, input().split())

    if ((p1 + p2) // k) % 2 == 0:
        print('CHEF')
    else:
        print('COOK')