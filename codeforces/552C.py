# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/9/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def binval(m, w):
    b = []
    while m > 0:
        b.append(m % w)
        m //= w
    
    return b
    

def solve(W, M):
    b = binval(M, W)
    
    if all([v <= 1 for v in b]):
        return True
    
    b += [0]
    for i in range(len(b)-1):
        v = b[i]
        if v > 1:
            v -= W
            if v != 0 and v != -1:
                return False
            b[i+1] += 1
    
    return True


W, M = map(int, input().split())
s = solve(W, M)
print('YES' if s else 'NO')
