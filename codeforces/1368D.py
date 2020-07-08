# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/30

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, A):
    M = 22
    bits = [0 for _ in range(M)]
    
    for v in A:
        i = 0
        while v > 0:
            if v & 1:
                bits[i] += 1
            v >>= 1
            i += 1
    
    ans = 0
    i = M-1
    while i >= 0:
        while bits[i] > 0:
            v = 0
            for j in range(i, -1, -1):
                if bits[j] > 0:
                    bits[j] -= 1
                    v |= 1 << j
            ans += v ** 2
        i -= 1
    
    return ans


if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]
    
    print(solve(N, A))