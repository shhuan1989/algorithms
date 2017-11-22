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
created by shhuan at 2017/11/22 00:42

"""



N, M = map(int, input().split())

# k // M + N >= K
# K + NM >= MK
# (M-1)K <= MN
# K <= NM/(M-1)

a = N*M
b = M - 1

if a % b == 0:
    print(a//b-1)
else:
    print(a//b)