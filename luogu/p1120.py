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
created by shhuan at 2020/7/15 09:57

"""

USED = [False for _ in range(100)]

def dfs(L, wait, needs, A, ai, first):
    if wait <= 0:
        return True

    if needs == 0:
        for i in range(len(A)):
            if not USED[i]:
                return dfs(L, wait-1, L, A, i, True)
        return True

    if needs < 0:
        return False

    for i in range(ai, len(A)) if not first else [ai]:
        if not USED[i] and A[i] <= needs:
            USED[i] = True
            if dfs(L, wait, needs-A[i], A, ai+1, False):
                return True
            USED[i] = False

    return False


if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]
    A = [x for x in A if x <= 50]
    A.sort(reverse=True)
    sa = sum(A)

    for l in range(A[0], sa//2+1):
        if sa % l != 0:
            continue
        if dfs(l, sa//l, l, A, 0, True):
            print(l)
            exit(0)
    print(sa)