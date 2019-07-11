# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-05-06

"""

import collections
import time
import os
import sys
import bisect
import heapq


def solve(points):
    # -x + y - c = 0, c > 0
    ans = float('inf')
    sp = sorted(points, key=lambda p: abs(p[1] - p[0] - 10**10))
    for i in range(len(sp)-1):
        x0, y0 = sp[i]
        x1, y1 = sp[i+1]
        x, y = (x0 + x1) / 2, (y0 + y1) / 2
        c = y-x
        
        ans = min(ans, abs(y1 - x1 - c))
    
    print(sp)
        
    # x + y - c = 0, c > 0
    sp = sorted(points, key=lambda p: abs(p[0] + p[1] - 10**10))
    for i in range(len(sp)-1):
        x0, y0 = sp[i]
        x1, y1 = sp[i + 1]
        x, y = (x0 + x1) / 2, (y0 + y1) / 2
        c = x + y
    
        ans = min(ans, abs(y1 + x1 - c))
        
    print(sp)
    
    print(ans)
    
    
T = int(input())
for ti in range(T):
    N = int(input())
    A = []
    for ni in range(N):
        x, y = map(int, input().split())
        A.append((x, y))
    solve(A)
    
    