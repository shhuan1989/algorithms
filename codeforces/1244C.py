# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/8/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, P, W, D):
    # x*W + y*D == P
    # 0 <= x < min(P//W, N)=10**12
    # 0 <= y < min(P//D, N)
    
    seen = set()
    x = 1
    us = []
    start = -1
    while True:
        v = P - x * W
        u = v % D
        if u in seen:
            start = us.index(u)
            break
        us.append(u)
        seen.add(u)
        x += 1

    if 0 not in seen:
        print(-1)
        return
    
    for i in range(start):
        x = i + 1
        if (P - x * W) % D == 0:
            y = (P - x * W) // D
            if y >= 0 and x + y <= N:
                print('{} {} {}'.format(x, y, N-x-y))
                return
    
    cycle = len(us) - start
    lo, hi = 0, P // W + 1
    while lo <= hi:
        m = (lo + hi) // 2
        for x in range(start + cycle * m, start + cycle * (m+1)):
            if (P - x * W) % D == 0:
                y = (P - x * W) // D
                if y < 0:
                    hi = m - 1
                elif x + y > N:
                    lo = m + 1
                else:
                    z = N - x - y
                    print('{} {} {}'.format(x, y, z))
                    return
                break
    print(-1)


N, P, W, D = map(int, input().split())
solve(N, P, W, D)