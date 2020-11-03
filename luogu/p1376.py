# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/27

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N, S = map(int, input().strip().split())
    C, Y = [], []
    for _ in range(N):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    
    
    
    ans = C[0] * Y[0]
    minpre = C[0]
    for i in range(1, N):
        minpre += S
        minpre = min(minpre, C[i])
        cost = minpre
        ans += minpre * Y[i]
    
    print(ans)