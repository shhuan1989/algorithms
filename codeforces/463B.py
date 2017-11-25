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
created by shhuan at 2017/11/24 23:37

"""


N = int(input())
A = [0] + [int(x) for x in input().split()]

energy = 0
ans = 0

for i in range(N):
    need = A[i+1] - A[i]
    if energy - need <= 0:
        d = need-energy
        energy = 0
        ans += d
    else:
        energy -= need

print(ans)