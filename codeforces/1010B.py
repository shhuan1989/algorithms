# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/18/18

"""

import collections
import time
import os
import sys
import bisect
import heapq


M, N = map(int, input().split())

lo, hi = 1, M + 1

cheat = [False] * N

for i in range(N):
    print('1')
    sys.stdout.flush()
    a = int(input())
    if a == 0:
        exit(0)
    elif a == -1:
        cheat[i] = True
    else:
        pass


qi = 0
while lo < hi:
    m = (lo + hi) // 2
    print(m)
    sys.stdout.flush()
    a = int(input())

    if cheat[qi]:
        a = -a

    if a == 0:
        exit(0)
    elif a < 0:
        hi = m
    else:
        lo = m + 1
        
    qi = (qi + 1) % N

print(lo)
sys.stdout.flush()


    
    


