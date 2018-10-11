# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 5/15/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


N = int(input()) + 1

if N == 1:
  print(0)
elif N % 2 == 0:
  print(N // 2)
else:
  print(N)
