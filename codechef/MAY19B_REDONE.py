# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-05-05

"""

import collections
import time
import os
import sys
import bisect
import heapq
import math

MOD = 10**9 + 7
MAXN = 1000000 + 10
F = [0] * MAXN
F[0] = 1

for i in range(1, MAXN):
    F[i] = (F[i-1] * i) % MOD

T = int(input())
for ti in range(T):
    N = int(input())
    print((F[N+1] - 1 + MOD) % MOD)