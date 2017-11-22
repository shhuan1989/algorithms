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
created by shhuan at 2017/11/21 22:28

"""

N = int(input())
S = input()


c = 0
p = ""
for v in S:
    if v == p:
        c += 1
    else:
        p = v

print(c)
