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
created by shhuan at 2020/7/24 18:10

"""



if __name__ == '__main__':
    N = int(input())
    W = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N):
        row = [int(x) for x in input().split()]
        for j, v in enumerate(row):
            W[i][i+j+1] = v
            W[i+j+1][i] = v


    k, sa, sb = 0, 0, 0
    for a in range(1, N+1):
        q = []
        for b in range(1, N+1):
            q.append((W[a][b], a, b))
        q.sort()

        if q[-2][0] > k:
            k, sa, sb = q[-2]

    print(1)
    print(k)


