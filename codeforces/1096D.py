# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/10/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


N = int(input())
S = input()
A = [int(x) for x in input().split()]

h, a, r, d = 0, 0, 0, 0

for i, v in enumerate(S):
    if v == 'h':
        h += A[i]
    elif v == 'a':
        a = min(h, a+A[i])
    elif v == 'r':
        r = min(a, r+A[i])
    elif v == 'd':
        d = min(r, d+A[i])

print(min(h, a, r, d))