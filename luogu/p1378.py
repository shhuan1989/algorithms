# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/28

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import itertools
import math

if __name__ == '__main__':
    # sys.stdin = open('P1378_2.in', 'r')
    N = int(input())
    x1, y1, x2, y2 = map(int, input().split())
    
    xline = [x1, x2]
    yline = [y1, y2]
    xline.sort()
    yline.sort()
    
    A = []
    for _ in range(N):
        x, y = map(int, input().split())
        if xline[0] <= x <= xline[1] and yline[0] <= y <= yline[1]:
            A.append((x, y))
    
    # print(xline)
    # print(yline)
    # print(A)

    def dist(x1, y1, x2, y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    
    def area(points):
        radius = []
        for i, (x, y) in enumerate(points):
            r = min(abs(v-x) for v in xline)
            r = min(r, min(abs(v-y) for v in yline))
            r = min(r, min([max(dist(x, y, points[j][0], points[j][1]) - radius[j], 0) for j in range(i)] or [float('inf')]))
            radius.append(r)
        a = min(xline[0], yline[0])
        b = max(xline[1], yline[1]) * 2
        a -= b
        
        # print(points, radius, math.pi * sum(r**2 for r in radius))
        return math.pi * sum(r**2 for r in radius)
    
    ans = max(area(points) for points in itertools.permutations(A))
    ans = (xline[1] - xline[0]) * (yline[1] - yline[0]) - ans
    print(round(ans))
    