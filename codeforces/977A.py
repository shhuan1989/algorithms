
# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/6/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, K):
    for i in range(K):
        d = N % 10
        if d > 0:
            N -= 1
        else:
            N //= 10
            
    return N

N, K = map(int, input().split())
print(solve(N, K))
