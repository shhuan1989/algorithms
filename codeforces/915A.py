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

N, K = map(int, input().split())

A = [int(x) for x in input().split()]

ans = float('inf')

for x in A:
  if K % x == 0:
    ans = min(ans, K // x)

print(ans)
