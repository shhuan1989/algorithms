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
created by shhuan at 2017/11/22 21:07

"""

N = int(input())

A = []

for i in range(N):
    A.append(list(input()))


found = False
for i in range(N):
    row = A[i]
    if row[0:2] == ['O', 'O']:
        row[0:2] = ['+', '+']
        found = True
        break
    if row[3:5] == ['O', 'O']:
        row[3:5] = ['+', '+']
        found = True
        break
if found:
    print("YES")
    for row in A:
        print("".join(row))
else:
    print("NO")