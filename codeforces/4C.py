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
created by shhuan at 2017/11/22 11:53

"""


N = int(input())

exists = collections.defaultdict(int)
for i in range(N):

    s = input()
    if s not in exists:
        print("OK")
        exists[s] = 1
    else:
        print(s+str(exists[s]))
        exists[s] += 1