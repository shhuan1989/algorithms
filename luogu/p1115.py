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
created by shhuan at 2020/7/15 22:40

"""


if __name__ == '__main__':
    N = int(input())
    A = []
    while len(A) < N:
        A += [int(x) for x in input().split()]

    presum = [0]
    for v in A:
        presum.append(presum[-1] + v)

    minv = float('inf')
    ans = float('-inf')
    for v in presum:
        ans = max(ans, v - minv)
        minv = min(minv, v)

    print(ans)
