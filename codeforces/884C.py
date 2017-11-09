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
created by shhuan at 2017/11/8 09:09



first step is merge two cycle that has maximum length(L+N),
a cycle has two parts with length L, N respectively  

----L--|----N------
        -         -
          -     -
             -
             
Then the convenience is N*N + (2*N+L+L)*L//2.
if two cycle have same length, choose the one has lower convenience to merge.

The second step is remove tail on the newly merged cycle.
convenience of this cycle changes from N*N + (2*N+L+L)*L//2 to (N+L)**2.



"""

N = int(input())
P = [0] + [int(x) for x in input().split()]


LN = []

C = []
vis = [0] * (N+1)
for i in range(1, N+1):
    if vis[i]:
        continue
    vis[i] = 1
    c = [i]
    while True:
        i = P[i]
        if not vis[i]:
            vis[i] = 1
            c.append(i)
        else:
            m = c.index(i)
            l, n = m, len(c)-m
            f = n**2 + (2*n+l+1)*l//2
            C.append((len(c), -f, c, i, l, n))
            break


C.sort(reverse=True)

if len(C) == 1:
    print(N*N)
    exit(0)

a = C[0]
b = C[1]
ans = (a[0] + b[0]) ** 2

for c in C[2:]:
    _, _, _, _, l, n = c
    ans += n**2 + (2*n+l+1)*l//2

print(ans)





