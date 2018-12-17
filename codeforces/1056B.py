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

N, M = map(int, input().split())


pairs = []
for x in range(1, M+1):
    for y in range(1, M+1):
        if (x**2+y**2) % M == 0:
            pairs.append((x, y))

ans = 0
segs = N // M
rem = N % M
ans = 0
for x, y in pairs:
    cx, cy = segs, segs
    if x <= rem:
        cx += 1
    if y <= rem:
        cy += 1
    ans += cx * cy

print(ans)
    
    
    
    
        