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
created by shhuan at 2020/7/11 18:54

"""

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    A = [int(x) for x in input().split()]


    def next_perm():
        for i in range(N-1, -1, -1):
            minv, mini = N+10, -1
            for j in range(i+1, N):
                if A[i] < A[j] < minv:
                    minv = A[j]
                    mini = j
            if mini >= 0:
                A[i], A[mini] = A[mini], A[i]
                A[i+1:] = A[i+1:][::-1]
                return

    for i in range(M):
        next_perm()

    print(' '.join(map(str, A)))