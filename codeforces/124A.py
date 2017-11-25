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
created by shhuan at 2017/11/23 22:45

"""

n, a, b = map(int, input().split())


ans = 0
for i in range(1, n+1):
    if i-1 >= a and n-i <= b:
        ans += 1

print(ans)