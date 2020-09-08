# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/2

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

if __name__ == '__main__':
    # sys.stdin = open('p1293.in')
    A = []
    for line in sys.stdin:
        a, b, c = line.strip().split()
        A.append((int(b), int(a), c))
    
    A.sort()
    
    def getcost(index):
        c = 0
        for i in range(N):
            c += abs(A[i][0] - A[index][0]) * A[i][1]
        return c
        
    
    
    N = len(A)
    ans = -1
    cost = float('inf')
    for i in range(N):
        c = getcost(i)
        if c < cost:
            cost = c
            ans = i
            
    print(A[ans][-1], cost)
    
    
    