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
created by shhuan at 2020/7/17 22:16

"""


def check(N, A, M):
    k = 0
    for i in range(N):
        k = (k + M - 1) % len(A)
        if A[k] == 1:
            return False

        A = A[:k] + A[k+1:]
        k %= len(A)

    return True

if __name__ == '__main__':
    N = int(input())

    A = [1 for _ in range(N)] + [0 for _ in range(N)]

    i = 1
    while True:
        if check(N, A, i):
            print(i)
            break
        i += 1