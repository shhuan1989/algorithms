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
    N = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))
    
    heapq.heapify(A)
    ans = 0
    while len(A) > 1:
        a = heapq.heappop(A)
        b = heapq.heappop(A)
        A.append(a+b)
        ans += a + b
    
    print(ans)