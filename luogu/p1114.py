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
created by shhuan at 2020/7/15 22:41

"""

if __name__ == '__main__':
    N = int(input())
    A = []
    while len(A) < N:
        A += [int(x) for x in input().split()]

    boys = [0]
    girls = [0]
    diff = [0]
    for v in A:
        if v == 1:
            boys.append(boys[-1] + 1)
            girls.append(girls[-1])
        else:
            girls.append(girls[-1] + 1)
            boys.append(boys[-1])
        diff.append(boys[-1] - girls[-1])

    di = {}
    ans = 0
    for i, v in enumerate(diff):
        if v in di:
            ans = max(ans, i-di[v])
        else:
            di[v] = i

    print(ans)
