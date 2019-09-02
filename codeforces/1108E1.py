# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2019/2/13 19:52

"""

N, M = map(int, input().split())
A = [int(x) for x in input().split()]
S = []
for i in range(M):
    l, r = map(int, input().split())
    S.append((l-1, r-1))


maxdiff = 0
ans = []
for i in range(N):
    a = [a for a in A]
    b = []
    for si, s in enumerate(S):
        if s[0] <= i <= s[1]:
            b.append(si+1)
            for j in range(s[0], s[1]+1):
                a[j] -= 1
    d = max(a) - min(a)
    if d > maxdiff:
        maxdiff = d
        ans = b

print(maxdiff)
print(len(ans))
print(' '.join(map(str, ans)))
