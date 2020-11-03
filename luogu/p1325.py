# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/9

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
    N, D = map(int, input().split())
    
    def getrange(x, y):
        l = math.sqrt(D ** 2 - y ** 2)
        return [x-l, x+l]
    
    points = []
    for _ in range(N):
        x, y = map(float, input().split())
        if y > D:
            print(-1)
            exit(0)
        l, r = getrange(x, y)
        points.append((r, l))
    
    
    points.sort()
    # print(points)
    ans = 1
    i = 0
    x = points[0][0]
    while i < N:
        # print(x)
        while i < N and points[i][1] <= x:
            i += 1
        if i < N:
            ans += 1
            x = points[i][0]
    
    print(ans)
    
    


    