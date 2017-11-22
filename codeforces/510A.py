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
created by shhuan at 2017/11/22 01:39

"""

N, M = map(int, input().split())

left = False
for i in range(1, N+1):
    if i % 2 == 1:
        print("#" * M)
    elif left:
        print("#" + "."*(M-1))
        left = False
    else:
        left = True
        print("."*(M-1) + "#")
