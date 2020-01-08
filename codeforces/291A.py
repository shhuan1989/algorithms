# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/7/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



N = int(input())
A = [int(x) for x in input().split()]
wc = collections.Counter([v for v in A if v != 0])

if any([c > 2 for c in wc.values()]):
    print(-1)
else:
    print(len([c for c in wc.values() if c == 2]))