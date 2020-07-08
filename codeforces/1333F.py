# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/1

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



if __name__ == '__main__':
    
    N = int(input())
    # t0 = time.time()
    maxdiv = [0 for _ in range(N+1)]
    maxdiv[1] = 1
    
    # print(time.time() - t0)
    
    for i in range(2, N+1):
        if maxdiv[i]:
            continue
        v = i
        d = 1
        while v <= N:
            if maxdiv[v] == 0:
                maxdiv[v] = d
            v += i
            d += 1
    
    # print(time.time() - t0)
    maxdiv = maxdiv[1:]
    maxdiv.sort()
    
    # print(time.time() - t0)
    ans = []
    maxd = 0
    for v in maxdiv:
        maxd = max(maxd, v)
        ans.append(maxd)
    
    print(' '.join(map(str, ans[1:])))
    
    # print(time.time() - t0)
