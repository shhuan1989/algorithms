# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/28

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
    A = set()
    for _ in range(N):
        A.add(input().strip())
    
    M = int(input())
    B = []
    for _ in range(M):
        B.append(input().strip())
    
    ina = set()
    for v in B:
        if v in A:
            ina.add(v)
            
    count = len(ina)
    if count == 0:
        print(0)
        print(0)
        exit(0)
    
    l, r = 0, 0
    ans = M
    wc = {}
    while r < M:
        v = B[r]
        if v in ina:
            wc[v] = wc.get(v, 0) + 1
            
            if len(wc) >= count:
                while l <= r:
                    u = B[l]
                    if u in ina:
                        if wc[u] > 1:
                            wc[u] -= 1
                        else:
                            break
                    l += 1
                # print(l, r)
                ans = min(ans, r-l+1)
        r += 1

    print(count)
    print(ans)
