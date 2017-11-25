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
created by shhuan at 2017/11/24 22:11

"""

na, nb = map(int, input().split())

k,  m = map(int, input().split())

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
A.sort()
B.sort(reverse=True)

if k > na or m > nb:
    print("NO")
else:
    if A[k-1] < B[m-1]:
        print("YES")
    else:
        print("NO")