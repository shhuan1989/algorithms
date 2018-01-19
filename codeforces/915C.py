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

a = [int(x) for x in input()]
b = [int(x) for x in input()]

ds = collections.Counter(a)
dsb = collections.Counter(b)

if ds == dsb:
  print(int(''.join(map(str, b))))
  exit(0)


if len(a) < len(b):
  ans = []
  for x in range(9, -1, -1):
    if x in ds and ds[x] > 0:
      ans.extend([x] * ds[x])
  print(''.join(map(str, ans)))
else:
  ans = float('-inf')

  for i in range(len(a)):
    dsc = {k:v for k, v in ds.items()}
    ansa = []
    for j, x in enumerate(b):
      mx = x
      my = 0 if j == 0 else -1
      if j < i:
        pass
      elif j == i:
        mx = x - 1
      else:
        mx = 9

      f = False
      for y in range(mx, my, -1):
        if y in ds and dsc[y] > 0:
          dsc[y] -= 1
          ansa.append(y)
          f = True
          break
      if not f:
        ansa = []
        break
    if ansa:
      # print(ansa)
      ans = max(ans, int(''.join(map(str, ansa))))

  if ans == float('-inf'):
    print(int(''.join(map(str, b))))
  else:
    print(ans)

