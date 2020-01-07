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
created by shhuan at 2019/12/30 19:51

"""


def solve(A):
    B = [v - i for i, v in enumerate(A)]
    C = [v + i for i, v in enumerate(A)]
    minval, mini = float('inf'), - 1
    for i, v in enumerate(B):
        if v > minval:
            return True, (mini + 1, i + 1)
        else:
            minval = v
            mini = i
    maxval, maxi = float('-inf'), - 1
    for i, v in enumerate(C):
        if v < maxval:
            return True, (maxi+1, i+1)
        else:
            maxval = v
            maxi = i
    return False, None


T = int(input())
ans = []
for ti in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    a, b = solve(A)
    if a:
        ans.append('YES')
        ans.append('{} {}'.format(b[0], b[1]))
    else:
        ans.append('NO')

print('\n'.join(ans))
