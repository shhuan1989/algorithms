# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/27

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
    MAXN = 10**N
    
    lp = [0 for _ in range(MAXN)]
    lp[0] = 2
    lp[1] = 2
    pr = []
    for i in range(2, MAXN):
        if lp[i] == 0:
            lp[i] = i
            pr.append(i)
        
        j = 0
        while j < len(pr) and pr[j] <= lp[i] and i*pr[j] < MAXN:
            lp[i*pr[j]] = pr[j]
            j += 1
            

    def dfs(curr, size):
        if size >= N:
            print(curr)
            return
        
        for i in range(10):
            u = curr * 10 + i
            if lp[u] == u:
                dfs(u, size+1)
                
    dfs(0, 0)
