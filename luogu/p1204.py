# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/3

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
    A = []
    for i in range(N):
        s, e = map(int, input().strip().split())
        A.append((s, 0))
        A.append((e+1, 1))
    A.sort()
    
    a, b = 0, 0
    c = 0
    start = 300
    for t, o in A:
        if c == 0:
            b = max(b, t-start+1)
            start = t
        if o == 0:
            c += 1
        else:
            c -= 1
        
        if c <= 0:
            a = max(a, t-start-1)
            c = 0
            start = t
    print('{} {}'.format(a, b))