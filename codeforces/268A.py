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
created by shhuan at 2017/11/22 01:03

"""

N = int(input())

H, A = [], []

for i in range(N):
    h, a = map(int, input().split())
    H.append(h)
    A.append(a)

ans = 0
for h in H:
    ans += A.count(h)

print(ans)