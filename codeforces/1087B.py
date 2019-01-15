# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/24/18

"""

import collections
import time
import os
import sys
import bisect
import heapq
import math

N, K = map(int, input().split())


ab = []
for i in range(1, min(int(math.sqrt(N)) + 2, K)):
    if N % i == 0:
        ab.append((i, N // i))


def solve(a, b):
    # x // k == a and x % k == b
    # x = y*k+b
    # ak <= x < (a+1)k
    # ak <= yk+b < (a+1)k
    # (ak-b)//k <= y < ((a+1)k-b)//k
    if b < K:
        for y in range((a*K-b)//K, ((a+1)*K-b)//K+1):
            x = y * K + b
            if x // K == a:
                return x
    
    return float('inf')
    
    
ans = float('inf')
for a, b in ab:
    
    ans = min(ans, solve(a, b), solve(b, a))

print(ans)
