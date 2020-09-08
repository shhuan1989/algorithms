# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/3

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    # sys.stdin = open('P1296_6.in', 'r')
    N, D = map(int, input().split())
    A = [int(x) for x in input().split()]
        
    A.sort()
    l, r = 0, 0
    ans = 0
    while r < N:
        if A[r]-A[l] > D:
            while l < r and A[r]-A[l] > D:
                ans += max(r-l-1, 0)
                l += 1
        r += 1
    
    while l < r:
        ans += max(r-l-1, 0)
        l += 1
    print(ans)