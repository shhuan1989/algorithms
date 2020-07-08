# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/16

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, K, A):
    A = [0 if v < K else (2 if v > K else 1) for v in A]
    if A.count(1) == 0:
        return False
    else:
        if N == 1:
            return True
        else:
            for i in range(N):
                if A[i] > 0 and any(A[j] > 0 for j in range(i + 1, min(i + 3, N))):
                    return True
    return False
    


T = int(input())
ans = []
for ti in range(T):
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    ans.append('yes' if solve(N, K, A) else 'no')

print('\n'.join(ans))