# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/30

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

v = []
v.append(0)
v.append(0)
v.append(0)
v.append(4)
v.append(4)
mod = int(1e9+7)
for i in range(5, 2000010):
    v.append(max(((2*v[i-2])+v[i-1])%mod,((4*v[i-4])+4*v[i-3]+v[i-2]+4)%mod))
t = int(input())
for _ in range(t):
    print(v[int(input())])