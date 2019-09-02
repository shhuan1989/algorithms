# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/28 23:02

"""
import math


T = int(input())

ans = []
for ti in range(T):
    ang = int(input())
    if 360 % (180-ang) == 0 and 360//(180-ang) > 2:
        ans.append(360//(180-ang))
    else:
        d = math.cos(math.radians(ang))
        alpha = math.asin(d)
        ans.append(2 * math.pi // alpha)

print('\n'.join(map(str, ans)))