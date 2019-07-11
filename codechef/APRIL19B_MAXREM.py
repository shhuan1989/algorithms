# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-04-07

"""

import collections
import time
import os
import sys
import bisect
import heapq


N = int(input())
A = set([-int(x) for x in input().split()])
if len(A) == 1:
    print(0)
else:
    A = list(A)
    heapq.heapify(A)
    
    heapq.heappop(A)
    a = heapq.heappop(A)
    
    print(abs(a))