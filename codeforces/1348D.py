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


def solve(N):
    A = [1]
    s = 1
    while s < N:
        A.append(A[-1] * 2)
        s += A[-1]
    
    if s > N:
        s -= A.pop()
        bisect.insort(A, N-s)

    return '\n'.join([str(len(A)-1), ' '.join(map(str, [b-a for a, b in zip(A[:-1], A[1:])]))])
    

if __name__ == '__main__':
    T = int(input())
    ans = []
    for ti in range(T):
        N = int(input())
        ans.append(solve(N))
    print('\n'.join(ans))
        