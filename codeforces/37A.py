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
created by shhuan at 2017/11/23 22:21

"""


N = int(input())
A = [int(x) for x in input().split()]

wc = collections.defaultdict(int)

for v in A:
    wc[v] += 1


print(max(wc.values()), len(wc))