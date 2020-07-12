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
created by shhuan at 2020/7/9 19:23

"""


def find(A, N, M):
    dpmax = [[0 for _ in range(M+1)] for _ in range(N+1)]
    dpmin = [[9 ** M + 1 for _ in range(M+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        s = sum(A[:i]) % 10
        dpmax[i][1] = s
        dpmin[i][1] = s

    for i in range(2, N+1):
        for j in range(2, min(i, M)+1):
            for pi in range(j-1, i):
                s = sum(A[pi: i]) % 10
                dpmax[i][j] = max(dpmax[i][j], dpmax[pi][j-1] * s)
                dpmin[i][j] = min(dpmin[i][j], dpmin[pi][j-1] * s)

    return dpmax[N][M], dpmin[N][M]


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(int(input()))

    maxv, minv = 0, 9 ** M + 1
    for i in range(N):
        A = A[i:] + A[:i]
        a, b = find(A, N, M)
        maxv = max(maxv, a)
        minv = min(minv, b)

    print(minv)
    print(maxv)
