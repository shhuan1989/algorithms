# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/11 23:12

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def dfs(A, l, r):
    if l >= r:
        return float('inf')

    m = (l + r) // 2
    a, b = dfs(A, l, m), dfs(A, m+1, r)
    d = min(a, b)
    ans = d
    x = (A[m][0] + A[m+1][0]) / 2
    for i in range(m, l-1, -1):
        if x - A[i][0] > d:
            break
        for j in range(m+1, r+1):
            if A[j][0] - x > d:
                break
            ans = min(ans, distance(A[i], A[j]))

    return ans


if __name__ == '__main__':
    N = int(input())
    A = []
    for i in range(N):
        x, y = map(int, input().strip().split())
        A.append((x, y))

    A.sort()

    print('{:.4f}'.format(dfs(A, 0, N-1)))