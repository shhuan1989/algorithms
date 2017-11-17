# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/5 15:00

"""

H, M, S, t1, t2 = map(int, input().split())


# 12 * 60 * 60 positions
h = (H % 12)*60*60 + M*60 + S
m = M*12*60 + S*12
s = S * 12 * 60

t1 = (t1 % 12) * 3600
t2 = (t2 % 12) * 3600

if t1 > t2:
    t1, t2 = t2, t1


if not (t1 < h < t2 or t1 < m < t2 or t1 < s < t2):
    print("YES")
    exit(0)

if not((t2 < h or h < t1) or (t2 < m or m < t1) or (t2 < s or s < t1)):
    print("YES")
    exit(0)

print("NO")



