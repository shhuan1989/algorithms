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


N, M = map(int, input().split())

ans = float('inf')
for i in range(N):
  a, b = map(int, input().split())
  ans = min(ans, a / b)

print(ans * M)
