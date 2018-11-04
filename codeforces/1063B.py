# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/11/3 19:10

"""

N, M = map(int, input().split())
R, C = map(int, input().split())
X, Y = map(int, input().split())

R -= 1
C -= 1

A = []
for i in range(N):
    A.append(list(input()))


q = collections.deque([(X, Y, R, C)])
visted = [[False for _ in range(M)] for _ in range(N)]
visted[R][C] = True
ans = 0
while q:
    x, y, r, c = q.popleft()
    A[r][c] = '+'
    ans += 1
    for nx, ny, nr, nc in [(x, y, r-1, c), (x, y, r+1, c), (x-1, y, r, c-1), (x, y-1, r, c+1)]:
        if nx >= 0 and ny >= 0 and 0 <= nr < N and 0 <= nc < M and A[nr][nc] == '.' and not visted[nr][nc]:
            visted[nr][nc] = True
            if nx < x or ny < y:
                q.append((nx, ny, nr, nc))
            else:
                q.appendleft((nx, ny, nr, nc))


# for row in A:
#     print(''.join(row))

print(ans)