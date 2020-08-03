# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/9

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

import math


def drop(h):
    return math.sqrt(2 * h / 10)


if __name__ == '__main__':
    H, S1, V, L, K, N = map(float, input().split())
    N = int(N)

    t1 = drop(H - K)
    t2 = drop(H)
    
    l = S1 - V * t2
    r = S1 + L - V * t1
    
    ans = 0
    for i in range(N):
        if abs(l-i) <= 0.0001 or abs(r-i) <= 0.0001 or l <= i <= r:
            ans += 1
    print(ans)
        
    