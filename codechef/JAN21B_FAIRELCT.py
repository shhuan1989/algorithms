# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2021/1/4

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List



def solve(N, M, A, B):
    sa, sb = sum(A), sum(B)
    if sa > sb:
        return 0
    
    A.sort()
    B.sort(reverse=True)
    ans = 0
    ai, bi = 0, 0
    while ai < N and bi < M:
        diff = A[ai] - B[bi]
        if diff >= 0:
            break
        
        sa -= diff
        sb += diff
        ans += 1
        if sa > sb:
            break
        ai += 1
        bi += 1
        
    return ans if sa > sb else -1
    
    

if __name__ == '__main__':
    T = int(input())
    for ti in range(T):
        N, M = map(int, input().split())
        A = [int(x) for x in input().split()]
        B = [int(x) for x in input().split()]
        print(solve(N, M, A, B))