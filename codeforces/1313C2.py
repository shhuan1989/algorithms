# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/3/2

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, A):
  maxv = max(A)
  left = [maxv for _ in range((N+1))]
  for i in range(N-1, -1, -1):
    left[i] = min(left[i+1], A[i])

  right = [0 for _ in range((N+1))]
  for i in range(1, N+1):
    right[i] = min(right[i-1], A[i-1])


  print(left)
  print(right)


N = int(input())
A = [int(x) for x in input().split()]

