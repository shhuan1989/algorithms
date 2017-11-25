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
created by shhuan at 2017/11/24 13:26

"""


N = int(input())

col = set()
row = set()

ans = []
for i in range(1, N**2+1):
    r, c = map(int, input().split())
    if r not in row and c not in col:
        ans.append(i)
        row.add(r)
        col.add(c)

print(" ".join(map(str, ans)))