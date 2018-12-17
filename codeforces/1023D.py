# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/14/18

"""

import collections
import time
import os
import sys
import bisect
import heapq


N, Q = map(int, input().split())
A = [int(x) for x in input().split()]

vis = collections.defaultdict(list)
for i, v in enumerate(A):
    if v > 0:
        vis[i].append(i)

