# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/12/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, K, C):
    MAXN = 1000005
    isp = [0 for _ in range(MAXN)]
    for i in range(2, MAXN):
        if isp[i] == 0:
            for j in range(i, MAXN, i):
                isp[j] = i

    cntp = [0 for _ in range(MAXN)]
    for i, v in enum
        while v > 1:
            p = isp[v]
            cnt = 0
            while v % p == 0:
                v //= p  l
                cnt += 1
            cntp[p] = max(cntp[p], cnt)
    
    ok = True
    while K > 1:
        ik = isp[K]
        ok = ok and (cntp[ik] > 0)
        cntp[ik] -= 1
        K //= ik
    
    return ok
            
    
    

N, K = map(int, input().split())
C = [int(x) for x in input().split()]
print('Yes' if solve(N, K, C) else 'No')