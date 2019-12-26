# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/25/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

N = int(input())
idx = [int(v) for v in input().split()]
idx.sort()
idx = [0] + idx
for i in range(N):
    if idx[i] < idx[i+1] - 1:
        print(idx[i]+1)
        exit(0)

print(N+1)