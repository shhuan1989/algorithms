# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/24/18

"""

import collections
import time
import os
import sys
import bisect
import heapq


p1 = [int(x) for x in input().split()]
p2 = [int(x) for x in input().split()]
p3 = [int(x) for x in input().split()]


def connect(pa, pb):
    xa, ya = pa
    xb, yb = pb
    minx, maxx = min(xa, xb), max(xa, xb)
    miny, maxy = min(ya, yb), max(ya, yb)
    l = abs(xa-xb) + abs(ya-yb) + 1
    ans = []
    
    if xa == xb:
        ans.append((l, [(xa, y) for y in range(min(ya, yb), max(ya, yb)+1)]))
    elif ya == yb:
        ans.append((l, [(x, ya) for x in range(min(xa, xb), max(xa, xb)+1)]))
    else:
        if xa > xb:
            xa, ya = pb
            xb, yb = pa
        
        if ya < yb:
            ans.append((l, [(x, miny) for x in range(minx, maxx + 1)] + [(maxx, y) for y in range(miny, maxy + 1)]))
            ans.append((l, [(minx, y) for y in range(miny, maxy+1)] + [(x, maxy) for x in range(minx, maxx+1)]))
        else:
            ans.append((l, [(maxx, y) for y in range(miny, maxy+1)] + [(x, maxy) for x in range(minx, maxx+1)]))
            ans.append((l, [(x, miny) for x in range(minx, maxx+1)]+ [(minx, y) for y in range(miny, maxy+1)]))
    
    return ans
    

minl = float('inf')
ans = []

for points in [list(sorted((p1, p2, p3)))]:
    p1, p2, p3 = points
    for l1, path1 in connect(p1, p2):
        l2 = float('inf')
        path2 = []
        for p in path1:
            for l3, path3 in connect(p, p3):
                if l3 < l2:
                    l2 = l3
                    path2 = path3
        l = l1+l2-1
        if l < minl:
            minl = l
            ans = path1 + path2

ans = set(ans)
print(len(ans))
print('\n'.join(['{} {}'.format(x, y) for x, y in ans]))



