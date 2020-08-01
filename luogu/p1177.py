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
created by shhuan at 2020/7/21 20:32

"""

import random

if __name__ == '__main__':
    # sys.stdin = open('p1177_1.in', 'r')
    N = int(input())
    A = []
    while len(A) < N:
        A += [int(x) for x in input().split()]

    # N = 10**5
    # A = [random.randint(0, 10**7) for _ in range(N)]
    # N = 100000
    # A = [1 for i in range(1, N+1)]
    def partition(l, r):
        mid = A[(l + r) // 2]
        i, j = l, r
        while i <= j:
            while i <= j and A[i] < mid:
                i += 1
            while i <= j and A[j] > mid:
                j -= 1
            if i <= j:
                A[i], A[j] = A[j], A[i]
                # 注意交换后改变i和j，否则可能死循环
                i += 1
                j -= 1
        return i

    def sort(l, r):
        if l >= r:
            return
        m = partition(l, r)

        sort(l, m-1)
        sort(m, r)

    sort(0, N-1)
    print(' '.join(map(str, A)))
