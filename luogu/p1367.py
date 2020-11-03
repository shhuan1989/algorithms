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


if __name__ == '__main__':
    N, T = map(int, input().strip().split())
    A = []
    for i in range(N):
        pos, d = map(int, input().split())
        A.append([pos, d, i])
    
    
    B = [[pos + d * T, d, i] for pos, d, i in A]
    A.sort()
    B.sort()
    
    crash = [False for _ in range(N)]
    for i in range(N):
        B[i][2] = A[i][2]
    
    for i in range(N):
        if i+1 < N and B[i][0] == B[i+1][0]:
            crash[B[i][2]] = True
            crash[B[i+1][2]] = True
    
    C = [(i, pos, d) for pos, d, i in B]
    C.sort()
    
    # print(C)
    # print(B)
    # print(crash)
    for id, pos, d in C:
        print(pos, d if not crash[id] else 0)