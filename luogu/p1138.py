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
created by shhuan at 2020/7/17 23:30

"""

if __name__ == '__main__':
    N, K = map(int, input().split())
    A = []
    while len(A) < N:
        A += [int(x) for x in input().strip().split()]

    V = [0 for _ in range(30010)]
    for v in A:
        V[v] |= 1

    for i in range(30010):
        if V[i] == 1:
            K -= 1
        if K == 0:
            print(i)
            exit(0)
    print('NO RESULT')