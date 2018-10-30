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
created by shhuan at 2017/12/2 22:37

"""


N, M, C = map(int, input().split())
ans = [0] * (N+1)

ls, le = 1, N+1
rs, re = N//2+1, N+1
for _ in range(M):
    p = int(input())

    ii = -1

    if p < C//2+1:
        for i in range(1, N+1):
            if ans[i] == 0 or ans[i] > p:
                ii = i
                break
    else:
        for i in range(N, 0, -1):
            if ans[i] == 0 or ans[i] < p:
                ii = i
                break

    ans[ii] = p
    print(ii)
    sys.stdout.flush()

    if all(x > 0 for x in ans[1:]):
        # print(ans)
        exit(0)