# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/1/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


N = int(input())
A = []
for i in range(N):
    A.append(list(input()))

M = len(A[0])
ans = 0

for r in range(N):
    for c in range(M):
        if A[r][c] == 'X' and all([0 <= nr < N and 0 <= nc < M and A[nr][nc] == 'X' for nr, nc in [(r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]]):
            ans += 1

print(ans)
