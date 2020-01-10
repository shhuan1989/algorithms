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


def solve(A):
    A = list(sorted(set(A)))

    ma = 2 * max(A)
    leftmax = [0 for i in range(ma + 1)]
    for v in A:
        leftmax[v] = v
    
    v = 0
    for i in range(ma + 1):
        nv = max(v, leftmax[i])
        leftmax[i] = v
        v = nv
    
    ans = 0
    for v in A:
        k = 2
        while k * v <= ma:
            u = k * v
            w = leftmax[u]
            ans = max(ans, w % v)
            k += 1
    
    return ans
    

N = int(input())
A = [int(x) for x in input().split()]
print(solve(A))