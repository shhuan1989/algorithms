# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2019/12/30 21:55

"""

N = int(input())
A = []
for i in range(N):
    x, y = map(int, input().split())
    A.append((x, y))

def dist(a, b):
    return (a[0]-b[0]) ** 2 + (a[1] - b[1]) ** 2

while True:
    a = {i for i in range(N) if A[i][0] % 2 == 0 and A[i][1] % 2 == 0}
    b = {i for i in range(N) if A[i][0] % 2 == 0 and A[i][1] % 2 == 1}
    c = {i for i in range(N) if A[i][0] % 2 == 1 and A[i][1] % 2 == 0}
    d = {i for i in range(N) if A[i][0] % 2 == 1 and A[i][1] % 2 == 1}

    if len([v for v in [a, b, c, d] if v]) == 1:
        A = [(x//2, y//2) for x, y in A]
        continue

    if not a and not d:
        ans = b
    elif not b and not c:
        ans = a
    else:
        ans = a | d
    ans = [i+1 for i in ans]
    print(len(ans))
    print(' '.join(map(str, ans)))
    exit(0)


