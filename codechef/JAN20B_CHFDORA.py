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
created by shhuan at 2020/1/4 14:55

"""


def manacher(row):
    nrow = len(row)
    m = [0 for _ in range(nrow)]

    # maxRight是已经触及的最右端点，pos是此时的中心位置
    maxRight, pos = 0, 0
    for i, v in enumerate(row):
        # 本问题只处理奇数长度，实际的Manacher可以通过添加#来把偶数长度变成奇数。
        # 注意右边这个min
        l = 1 if i >= maxRight else min(m[pos*2-i], maxRight-i)
        while i + l < nrow and i - l >= 0 and row[i + l] == row[i - l]:
            l += 1
        l -= 1
        m[i] = l

        # 值有大于的时候才需要更新pos
        if i + l > maxRight:
            maxRight = i + l
            pos = i
    return m


def solve(A, N, M):
    manacherRow = []
    for row in A:
        manacherRow.append(manacher(row))

    manacherCol = [[0 for _ in range(M)] for _ in range(N)]
    for c, col in enumerate([[A[r][c] for r in range(N)] for c in range(M)]):
        m = manacher(col)
        for r, v in enumerate(m):
            manacherCol[r][c] = v

    ans = M * N
    for r in range(N):
        for c in range(M):
            ans += min(manacherRow[r][c], manacherCol[r][c])

    return ans


T = int(input())
for ti in range(T):
    N, M = map(int, input().split())
    A = []
    for r in range(N):
        row = [int(x) for x in input().split()]
        A.append(row)
    print(solve(A, N, M))




