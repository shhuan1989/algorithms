# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/24

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [int(x) for x in input().split()]
    
    q = A[:M]
    heapq.heapify(q)
    ai = M
    ans = 0
    while q:
        t = heapq.heappop(q)
        if ai < N:
            heapq.heappush(q, t+A[ai])
            ai += 1
        ans = t
    
    print(ans)
