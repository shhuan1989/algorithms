# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/3/13

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, dest):

  stopped = collections.defaultdict(set)
  incycle = []

  for r in range(N):
    for c in range(N):
      a, b = dest[r][c]
      if a == -1:
        incycle.append((r, c))
      else:
        stopped[a-1, b-1].add((r, c))

  mark = [['' for _ in range(N)] for _ in range(N)]
  for k, points in stopped.items():
    r, c = k
    if mark[r][c] != '':
      return 'INVALID'
    mark[r][c] = 'X'
    points.discard(k)

    q = [k]
    while q:
      nq = []
      for r, c in q:
        for nr, nc, x in [(r-1, c, 'D'), (r+1, c, 'U'), (r, c-1, 'R'), (r, c+1, 'L')]:
          key = (nr, nc)
          if key in points:
            nq.append(key)
            points.remove(key)
            if mark[nr][nc] == '':
              mark[nr][nc] = x
            elif mark[nr][nc] != x:
              return 'INVALID'
      q = nq

    if points:
      return 'INVALID'

  if incycle:
    ncycle = len(incycle)
    ci = {}
    for i, v in enumerate(incycle):
      ci[v] = i
    paired = [i for i in range(ncycle)]

    for i, (r, c) in enumerate(incycle):
      if paired[i] != i:
        continue

      for nr, nc, a, b in [(r-1, c, 'U', 'D'), (r+1, c, 'D', 'U'), (r, c-1, 'L', 'R'), (r, c+1, 'R', 'L')]:
        key = (nr, nc)
        if key in ci:
          pi = ci[key]
          if paired[pi] == pi:
            paired[i] = pi
            paired[pi] = i
            if mark[r][c] == '' or mark[r][c] == a:
              mark[r][c] = a
            else:
              return 'INVALID'
            if mark[nr][nc] == '' or mark[nr][nc] == b:
              mark[nr][nc] = b
            else:
              return 'INVALID'
            break

    unpaired = [i for i in range(ncycle) if paired[i] == i]
    for i in unpaired:
      r, c = incycle[i]
      for nr, nc, a, b in [(r-1, c, 'U', 'D'), (r+1, c, 'D', 'U'), (r, c-1, 'L', 'R'), (r, c+1, 'R', 'L')]:
        key = (nr, nc)
        if key in ci:
          if mark[r][c] == '' or mark[r][c] == a:
            mark[r][c] = a
          else:
            return 'INVALID'
          paired[i] = ci[key]
          break

    if [i for i in range(ncycle) if paired[i] == i]:
      return 'INVALID'


  return 'VALID\n' + '\n'.join([''.join(row) for row in mark])



N = int(input())

dest = [[(r, c) for c in range(N)] for r in range(N)]
for r in range(N):
  row = [int(x) for x in input().split()]
  for i in range(0, len(row), 2):
    dest[r][i//2] = (row[i], row[i+1])

print(solve(N, dest))


