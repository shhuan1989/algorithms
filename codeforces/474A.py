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
created by shhuan at 2017/11/22 22:23

"""

keyboard = [
    "qwertyuiop",
    "asdfghjkl;",
    "zxcvbnm,./"
]

R = {}
L = {}
for row in keyboard:
    for i in range(1, len(row)):
        R[row[i]] = row[i-1]
    R[row[0]] = row[0]

    for i in range(len(row)-1):
        L[row[i]] = row[i+1]
    L[row[-1]] = row[-1]


lr = input()
s = input()
if lr == "R":
    ans = "".join([R[v] for v in s])
    print(ans)
else:
    ans = "".join([L[v] for v in s])
    print(ans)


