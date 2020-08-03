# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/31

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
    A = []
    for i in range(N):
        row = list(input().strip())
        A.append(row)

    s = 'hehe'
    t = 'eheh'
    
    ans = 0
    for r in range(N):
        for c in range(M):
            if c+4 <= M and ''.join(A[r][c: c+4]) in {s, t}:
                ans += 1
            if r+4 <= N and ''.join([A[nr][c] for nr in range(r, r+4)]) in {s, t}:
                ans += 1
    
    print(ans)
    