# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/11/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

N = int(input())

children = collections.defaultdict(set)
leaves = {i for i in range(1, N+1)}

for u in range(2, N+1):
  v = int(input())
  children[v].add(u)
  leaves.discard(v)

for v, us in children.items():
  if us and len({u for u in us if u in leaves}) < 3:
    print("NO")
    # print(v, us)
    exit(0)

print("YES")
