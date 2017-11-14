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
    ones = [0] * N
    for c in range(N // 4):
        v = tob(a[r][c])
        for i in range(4):
            if v[i] == '1':
                ones[c*4+i] = 1

    groups = set()
    if ones[0] != 0:
        groups.add(1)
    for i in range(1, N):
        if ones[i] == 1:
            if ones[i-1] != 0:
                ones[i] = ones[i-1]
            else:
                ones[i] = i + 1
                groups.add(i + 1)

    return ones, groups

def one_index2(a, r):
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


last_ones, last_groups = one_index(A, 0)
for r in range(1, M):
    ones, groups = one_index(A, r)
    rep = {}
    for i in range(N):
        x, y = last_ones[i], ones[i]
        if x != 0 and y != 0:
            if x not in rep:
                rep[x] = y
            else:
                rep[x] = min(rep[x], y)

    for i in range(N):
        x, y = last_ones[i], ones[i]
        if x != 0 and y != 0:
            last_groups -= {x}
            rx = rep[x]
            if y != rx:
                groups -= {y}
                ones[i] = rx
                j = i-1
                while j >= 0 and ones[j] != rx and ones[j] != 0:
                    ones[j] = rx
                    j -= 1
                j = i+1
                while j < N and ones[j] != rx and ones[j] != 0:
                    ones[j] = rx
                    j += 1

    ans += len(last_groups)
    last_ones, last_groups = ones, groups


print(ans + len(last_groups))



