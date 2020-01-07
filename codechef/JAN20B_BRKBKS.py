# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/1/4 11:44

"""


T = int(input())
for ti in range(T):
    A = [int(x) for x in input().split()]
    S = A[0]
    A = A[1:]

    if sum(A) <= S:
        print(1)
    elif A[0] + A[1] <= S or A[1] + A[2] <= S:
        print(2)
    else:
        print(3)