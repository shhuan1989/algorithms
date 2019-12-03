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
created by shhuan at 2019/11/30 16:11

"""
import sys
sys.setrecursionlimit(10**5+5)

L = [int(x) for x in input().split()]
N = L[0]
A, P = [0] + L[1: N+1], [0] + L[N+1:]

T = collections.defaultdict(list)
root = -1
for i in range(1, N+1):
    if P[i] == -1:
        root = i
    T[P[i]].append(i)

def dfs(node):
    if not node:
        return float('inf'), float('-inf')

    minval, diff = A[node], float('-inf')

    for sub in T[node]:
        mv, df = dfs(sub)
        minval = min(minval, mv)
        diff = max(diff, df)
    diff = max(diff, A[node] - minval)

    return minval, diff

minval, diff = dfs(root)
print(diff)


