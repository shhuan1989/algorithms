# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/21

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def dist(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

if __name__ == '__main__':
    x1, y1, x2, y2 = map(int, input().strip().split())
    N = int(input())
    
    points = []
    for i in range(N):
        x, y = map(int, input().strip().split())
        points.append((x, y, i))
    
    ra = [(dist(x, y, x1, y1), i) for x, y, i in points]
    rb = [(-dist(x, y, x2, y2), i) for x, y, i in points]
    
    ra.sort()
    heapq.heapify(rb)
    
    ans = float('inf')
    visa = set()
    for da, ia in ra:
        visa.add(ia)
        
        while rb and rb[0][1] in visa:
            heapq.heappop(rb)
            
        ans = min(ans, da + (abs(rb[0][0]) if rb else 0))

    print(ans)