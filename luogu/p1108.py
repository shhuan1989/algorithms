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
created by shhuan at 2020/7/12 19:37

"""

def solve(N, A):
    dpa = [0 for _ in range(N)]
    dpb = [0 for _ in range(N)]
    ans = 0
    ansb = 0
    for i, v in enumerate(A):
        pv = set()
        maxl = 1
        count = 0
        for j in range(i - 1, -1, -1):
            u = A[j]
            if u > v and u not in pv:
                d = dpa[j] + 1
                if d > maxl:
                    maxl = d
                    count = dpb[j]
                elif d == maxl:
                    count += dpb[j]
                pv.add(u)
        dpb[i] = max(count, 1)
        dpa[i] = maxl
        ans = max(ans, maxl)

    # print(dpa)
    # print(dpb)
    pv = set()
    for i in range(N - 1, -1, -1):
        if dpa[i] == ans and A[i] not in pv:
            ansb += dpb[i]
            pv.add(A[i])

    print('{} {}'.format(ans, ansb))


if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]
    while len(A) < N:
        A += [int(x) for x in input().split()]
    solve(N, A)

    # import random
    # for i in range(1000):
    #     N = random.randint(2000, 6000)
    #     A = [random.randint(0, 2 ** 16) for _ in range(N)]
    #     solve(N, A)
