# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/12/19

"""

import collections
import time
import os
import sys
import bisect
import heapq

N, K, M = map(int, input().split())

A = [int(x) for x in input().split()]
A.sort()

S = [0] * (N+1)
for i in range(N-1, -1, -1):
    S[i] = S[i+1] + A[i]

ans = 0
for l in range(min(N, M+1)):
    r = N-l
    incr = min(M-l, r * K)
    ans = max(ans, (S[l] + incr) / r)

print(ans)