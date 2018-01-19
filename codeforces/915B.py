# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/16/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


n, pos, l, r = map(int, input().split())

ans = float('inf')
q = [(1, n, pos, 0)]
vis = {(1, n, pos)}
while q:
  a, b, p, c = q.pop(0)
  # print(a, b, p, c)
  if a == l and b == r:
    ans = min(ans, c)
  else:
    # move to left
    if p > l:
      if (a, b, p-1) not in vis:
        q.append((a, b, p-1, c+1))
        vis.add((a, b, p-1))

    # move to right
    if p < r:
      if (a, b, p+1) not in vis:
        q.append((a, b, p+1, c+1))
        vis.add((a, b, p+1))

    # close right
    if p >= r and b > r:
      if (a, p, p) not in vis:
        q.append((a, p, p, c+1))
        vis.add((a, p, p))

    # close left
    if p >= l and a < l:
      if (p, b, p) not in vis:
        q.append((p, b, p, c+1))
        vis.add((p, b, p))

print(ans)


