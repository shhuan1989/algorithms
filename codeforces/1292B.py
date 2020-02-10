# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/7/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def getpoints(x0, y0, ax, ay, bx, by, xs, ys, t):
    s = [(x0, y0)]
    
    x, y = x0, y0
    while True:
        x = ax*x + bx
        y = ay*y + by
        
        # print(x, y)
        
        if x > xs + t or y > ys + t:
            break
        s.append((x, y))
    
    return s


def solve(x0, y0, ax, ay, bx, by, xs, ys, totaltime):
    points = getpoints(x0, y0, ax, ay, bx, by, xs, ys, totaltime)
    
    ans = 0
    for start in range(len(points)):
        x, y = points[start]
        d = dist(x, y, xs, ys)
        t = totaltime
        if d > t:
            continue
        t -= d
        count = 1
        
        for i in range(start-1, -1,  -1):
            nx, ny = points[i]
            d = dist(x, y, nx, ny)
            if d > t:
                break
            count += 1
            t -= d
            x, y = nx, ny
        
        ans = max(ans, count)
        
        count = 1
        for i in range(start + 1, len(points)):
            nx, ny = points[i]
            d = dist(x, y, nx, ny)
            if d > t:
                break
            count += 1
            t -= d
            x, y = nx, ny
        ans = max(ans, count)
        
    
    return ans
    

x0, y0, ax, ay, bx, by = map(int, input().split())
xs, ys, t = map(int, input().split())

print(solve(x0, y0, ax, ay, bx, by, xs, ys, t))
