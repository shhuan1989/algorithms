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
created by shhuan at 2020/1/10 22:02

"""


def solve(N, A):
    yasser = sum(A)
    presum = [0 for _ in range(N+1)]
    for i, v in enumerate(A):
        presum[i + 1] = presum[i] + A[i]

    if any([presum[i] >= yasser for i in range(1, N)]) or any([v > yasser for v in A]):
        return 'NO'

    rightmax = [i for i in range(N+1)]
    for i in range(N-1, -1, -1):
        if presum[i] <= presum[rightmax[i+1]]:
            rightmax[i] = rightmax[i+1]

    for i in range(1, N+1):
        j = rightmax[i]
        if j > i and j-i < N and presum[j] - presum[i] >= yasser:
            return 'NO'

    return 'YES'


def test():
    N = random.randint(2, 10)
    A = [random.randint(-10, 10) for i in range(N)]
    print(N)
    print(A)
    print(sum(A))
    print(solve(N, A))

# test()

T = int(input())
ans = []
for ti in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    ans.append(solve(N, A))

print('\n'.join(ans))