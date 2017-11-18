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
created by shhuan at 2017/11/17 22:40

"""

N = int(input())
C = [int(x) for x in input().split()]

# N = 10**6
# C = [random.randint(1, 10**9) for _ in range(N)]
#
# t0 = time.time()


ans = 0
p = N
for i in range(N-1, -1, -1):
    # i-C[i], i-1
    if C[i] > 0 and p >= i-C[i]:
        # dead.append([max(i-C[i], 0), i-1])
        l, r = max(i-C[i], 0), i-1
        p = min(p, r)
        ans += max(p+1-l, 0)
        p = min(l-1, p)

        if l == 0:
            break

print(N - ans)


#
# print(time.time() - t0)




