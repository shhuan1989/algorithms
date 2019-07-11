# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-04-30

"""

import collections
import time
import os
import sys
import bisect
import heapq


N, M, R = map(int, input().split())

S = min([int(x) for x in input().split()])
T = max([int(x) for x in input().split()])

ans = T*(R//S) + R % S
print(max(R, ans))
