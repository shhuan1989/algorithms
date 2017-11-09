# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/8 09:50

"""

M, N = map(int, input().split())

A = []
for i in range(M):
    A.append(list(input()))


def tob(valChar):
    v = int(valChar, 16)
    v = bin(v)
    v = list(v[2:])
    v = ['0'] * (4-len(v)) + v
    return v

def one_index(a, r):
    ones = []
    for c in range(N // 4):
        v = tob(a[r][c])
        t = []
        for i in range(4):
            if v[i] == '1':
                j = c * 4 + i
                if t and t[-1][1] == j - 1:
                    u = t.pop()
                    t.append((u[0], j))
                else:
                    t.append((j, j))
        if t:
            if ones and ones[-1][1] == t[0][0] - 1:
                u = ones.pop()
                ones.append((u[0], t[0][1]))
                for u in t[1:]:
                    ones.append(u)
            else:
                for u in t:
                    ones.append(u)
    return ones

ans = 0

last_ones = one_index(A, 0)
for r in range(1, M):
    ones = one_index(A, r)

    # merge
    for one in last_ones:
        # if one not in ones, ans += 1
        m = bisect.bisect_right(ones, one)
        inone = False
        if 0 <= m <= len(ones):
            if m > 0 and ones[m-1][1] >= one[0] >= ones[m-1][0]:
                inone = True
            elif m < len(ones) and ones[m][0] <= one[1]:
                inone = True
        if not inone:
            ans += 1

    last_ones = ones


print(ans + len(last_ones))



