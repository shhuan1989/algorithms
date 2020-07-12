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
created by shhuan at 2020/7/11 18:22

"""


if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]

    dpa = [1 for _ in range(N)]
    dpb = [1 for _ in range(N)]
    for i in range(N):
        for j in range(i):
            dpa[i] = max(dpa[i], (1 + dpa[j]) if A[i] > A[j] else 0)

    for i in range(N-1, -1, -1):
        for j in range(i+1, N):
            dpb[i] = max(dpb[i], (1 + dpb[j]) if A[i] > A[j] else 0)


    # print(dpa)
    # print(dpb)

    ans = max([dpa[i] + dpb[i] - 1 for i in range(N)])
    print(N - ans)

