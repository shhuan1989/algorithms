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
created by shhuan at 2017/11/24 21:06

"""

a, b = map(int, input().split())

n = int(input())

ans = float('inf')

for i in range(n):
    x, y, v = map(int, input().split())

    t = math.sqrt((x-a)**2 + (y-b)**2) / v
    ans = min(t, ans)


print(ans)