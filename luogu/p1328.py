# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/10

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N, NA, NB = map(int, input().split())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    
    vs = [
        [0, 0, 1, 1, 0],
        [1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 0, 1],
        [1, 1, 0, 0, 0]
    ]
    
    sa, sb = 0, 0
    for i in range(N):
        a = A[i % NA]
        b = B[i % NB]
        sa += vs[a][b]
        sb += vs[b][a]
    
    print(sa, sb)
        