# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/21

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

import math
if __name__ == '__main__':
    points = []
    for _ in range(4):
        line = input().strip()
        line = line.replace('(', '')
        line = line.replace(')', '')
        x, y = [int(x) for x in line.split(',')]
        points.append((x, y))
    
    
    def dist(p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    
    def area(vertex):
        a, b, c = vertex[0], vertex[1], vertex[2]
        dab = dist(a, b)
        dbc = dist(b, c)
        dac = dist(a, c)
        p = (dab + dbc + dac) / 2
        
        return math.sqrt(max(p*(p-dab)*(p-dac)*(p-dbc), 0))
    
    def online(p1, p2, p3):
        return abs(dist(p1, p3) + dist(p2, p3) - dist(p1, p2)) < 1e-7
    
    
    a = area(points[:3])
    b = area(points[:2] + [points[3]])
    c = area(points[1: 3] + [points[3]])
    d = area([points[0], points[2], points[3]])
    
    # print(b, c, d, b+c+d, a)
    if abs(b+c+d-a) > 1e-7:
        print(2)
    else:
        if points[3] in points[:3]:
            print(4)
        elif online(points[0], points[1], points[3]) or online(points[0], points[2], points[3]) or online(points[1], points[2], points[3]):
            print(3)
        else:
            print(1)
    