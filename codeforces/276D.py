# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/30/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

L, R = map(int, input().split())


for i in range(64, -1, -1):
    if L & (1 << i) != R & (1 << i):
        print((1 << (i+1)) - 1)
        exit(0)
print(0)