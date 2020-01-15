# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/13/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, A, B):
    MOD = 998244353
    # A.sort()
    C = [A[i-1] * i * (N-i+1) for i in range(1, N+1)]
    C.sort()
    # print(C)
    B.sort(reverse=True)
    ans = 0
    for b, c in zip(B, C):
        ans += b * c
        ans %= MOD
    
    return ans


N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
print(solve(N, A, B))