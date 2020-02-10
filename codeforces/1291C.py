# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/3/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



def solve(N, M, K, A):

    if K >= M-1:
        return max(max(A[:M]), max(A[-M:]))
    
    uncontrol = M - 1 - K
    ans = 0
    for leftcontrl in range(K+1):
        tmp = float('inf')
        rightcontrol = K - leftcontrl
        for leftother in range(uncontrol+1):
            front = A[leftcontrl + leftother]
            rightother = uncontrol - leftother
            tail = A[-(rightcontrol + rightother + 1)]
            tmp = min(tmp, max(front, tail))
        ans = max(ans, tmp)
    
    
        
    return ans


T = int(input())
ans = []
for ti in range(T):
    N, M, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    ans.append(solve(N, M, K, A))

print('\n'.join(map(str, ans)))

