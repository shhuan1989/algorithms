# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/2/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

# N, M, K = map(int, input().split())
# A = []
# for r in range(N):
#   row = [[1, 1] if x == '.' else -1 for x in input()]
#   A.append(row)


N, M, K = 2000, 2000, 23
A = []
for _ in range(N):
  row = [[1, 1] if random.randint(0, 10) < 7 else -1 for _ in range(M)]
  A.append(row)

t0 = time.time()

ans = 0
for r in range(N):
  for c in range(M):
    if A[r][c] == -1:
      pass
    else:
      if r > 0 and A[r-1][c] != -1:
        A[r][c][0] = A[r-1][c][0] + 1
      if c > 0 and A[r][c-1] != -1:
        A[r][c][1] = A[r][c-1][1] + 1

      if r >= N-1 or A[r+1][c] == -1:
        ans += max(0, A[r][c][0] - K + 1)

      if c >= M-1 or A[r][c+1] == -1:
        ans += max(0, A[r][c][1] - K + 1)

print(ans)


print(time.time() - t0)
