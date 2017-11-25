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
created by shhuan at 2017/11/24 23:13

"""

N = int(input())
A = [int(x) for x in input().split()]

c = sum(A[::3] or [0])
b = sum(A[1::3] or [0])
p = sum(A[2::3] or[0])

m = max(c, b, p)
if m == c:
    print("chest")
elif m == b:
    print("biceps")
else:
    print("back")
