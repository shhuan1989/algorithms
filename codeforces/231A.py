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
created by shhuan at 2017/11/21 20:30

"""

N = int(input())

ans = 0
for i in range(N):
    s = [int(x) for x in input().split()]
    if s.count(1) > 1:
        ans += 1

print(ans)