# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/24

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    A = []
    for i in range(N):
        row = [int(x) for x in list(input().strip())]
        A.append(row)
    
    s = 0
    for r in range(N):
        for c in range(M):
            if A[r][c] > 0:
                s += 1
    s *= 2
    # left right
    for r in range(N):
        h = 0
        for c in range(M):
            s += abs(h - A[r][c])
            h = A[r][c]
        s += h
        
    # top down
    for c in range(M):
        h = 0
        for r in range(N):
            s += abs(h - A[r][c])
            h = A[r][c]
        s += h
    
    print(s)
    
    