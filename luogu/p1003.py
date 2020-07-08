# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/7

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
        a, b, g, k = map(int, input().split())
        A.append((a, b, g, k))
    
    x, y = map(int, input().split())
    
    ans = -1
    for i in range(N):
        a, b, g, k = A[i]
        if a <= x <= a+g and b <= y <= b+k:
            ans = i+1
    
    print(ans)