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
    A = [int(x) for x in input().split()]
    while len(A) < N:
        A += [int(x) for x in input().split()]
    vi = {v: i for i, v in enumerate(A)}
    A.sort()
    
    to = [i for i in range(N)]
    for i, v in enumerate(A):
        to[vi[v]] = i
        
    # print(to)
    ans = 0
    mark = [False for _ in range(N)]
    for i in range(N):
        if not mark[i]:
            j = i
            c = 0
            while not mark[j]:
                c += 1
                mark[j] = True
                j = to[j]
            ans += c - 1
    
    print(ans)
    
    