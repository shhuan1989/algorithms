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
created by shhuan at 2020/7/12 19:35

"""

if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]
    L, R = map(int, input().split())

    if sum(A) > N * R or sum(A) < N * L:
        print(-1)
        exit(0)

    a, b = 0, 0
    for v in A:
        if v > R:
            a += v - R
        elif v < L:
            b += L - v

    ans = max(a, b)
    print(ans)
