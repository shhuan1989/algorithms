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
created by shhuan at 2017/11/19 21:53


                                           1
                                     /         \ 
                            2                           3
                       /      \                     /       \
                  4              5             6                7
                  
                  
it forms a nearly complete binary tree.

parent(i) = i // 2
children(i) = {2*i, 2*i+1}

dist(i, 2*i) = L(2*i-1)
dist(i, 2*i+1) = L(2*i)












"""

N, M = map(int, input().split())

L = [0] * (N+5)
A = collections.defaultdict(list)

for i in range(2, N+1):
    L[i] = int(input())

for i in range(1, N+1):
    d = 0
    u = i
    while u > 0:
        A[u].append(d)
        d += L[u]
        u //= 2

presum = [[] for _ in range(N+1)]
for i in range(1, N+1):
    A[i].sort()

    presum[i] = [0] * (len(A[i]) + 1)
    for j in range(len(A[i])):
        presum[i][j+1] = presum[i][j] + A[i][j]

def solve(a, h):
    # sum all value of node in subtree of a
    if a > N or a < 1 or h < 0:
        return 0

    p = bisect.bisect_left(A[a], h)

    return p * h - presum[a][p]

for i in range(M):
    a, h = map(int, input().split())
    ans = solve(a, h)

    while a != 1:
        fa = a//2
        h -= L[a]
        if h < 0:
            break
        else:
            ans += h

        if a == 2 * fa and 2*fa + 1 <= N:
            # a is left child of father
            ans += solve(2*fa+1, h-L[2*fa+1])
        if a == 2 * fa + 1:
            # a is right child of father
            ans += solve(2*fa, h-L[2*fa])
        a = fa

    print(ans)






