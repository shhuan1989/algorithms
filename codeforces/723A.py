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
created by shhuan at 2017/11/22 11:32

"""


# sum(abs(xi - x))


A = [int(x) for x in input().split()]


ans = float('inf')
for i in range(max(A)+1):

    t = sum([abs(v-i) for v in A])
    ans = min(ans, t)

print(ans)