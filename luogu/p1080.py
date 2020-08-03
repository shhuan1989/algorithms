# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/13

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
    for i in range(N+1):
        a, b = map(int, input().split())
        A.append((a, b))
    
    B = [(A[i][0] * A[i][1], A[i][1], A[i][0], i) for i in range(1, N+1)]
    B.sort()
    
    # print([(a, b, i) for b, a, i in B])
    s = A[0][0]
    ans = 0
    for c, b, a, i in B:
        ans = max(ans, s//b)
        s *= a
    
    print(ans)
