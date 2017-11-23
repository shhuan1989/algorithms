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
created by shhuan at 2017/11/22 12:56

"""


ans = 0
police = 0

N = int(input())
A = [int(x) for x in input().split()]

for v in A:
    police += v
    if police < 0:
        police = max(police, 0)
        ans += 1

print(ans)