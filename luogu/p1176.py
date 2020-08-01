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
created by shhuan at 2020/7/21 21:05

"""


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [[True for _ in range(N)] for _ in range(N)]
    for i in range(M):
        x, y = map(int, input().split())
        A[x-1][y-1] = False


    MOD = 100003
    W = [[0 for _ in range(N)] for _ in range(N)]
    W[0][0] = 1

    for x in range(N):
        for y in range(N):
            if not A[x][y]:
                continue

            if y > 0:
                W[x][y] += W[x][y-1]
                W[x][y] %= MOD

            if x > 0:
                W[x][y] += W[x-1][y]
                W[x][y] %= MOD

    print(W[N-1][N-1])