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
created by shhuan at 2017/11/22 12:55

"""

A = [int(x) for x in input().split()]

N = len(A)

s = sum(A)

if s > 0 and s % N == 0:
    print(s // N)
else:
    print(-1)