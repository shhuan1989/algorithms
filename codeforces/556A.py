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
created by shhuan at 2017/11/22 21:44

"""

N = int(input())
A = list(input())

S = []

for i, v in enumerate(A):
    if S and S[-1] != v:
        S.pop()
    else:
        S.append(v)

print(len(S))