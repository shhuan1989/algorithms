# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/4

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def gcd(x, y):
    while y:
        x, y = y, x%y
    
    return x


def lcm(a, b):
    c = gcd(a, b)
    return a * b // c


def solve(N, M, A, B):
    if N * A != M * B:
        return False, []
    
    d = lcm(N, M) // N
    matrix = [[0 for _ in range(M)] for _ in range(N)]
    cs = 0
    for r in range(N):
        for c in range(cs, min(cs+A, M)):
            matrix[r][c] = 1
        for c in range(0, A-(M-cs)):
            matrix[r][c] = 1
        cs = (cs + d) % M
    
    return True, matrix
    
    
    


T = int(input())
for ti in range(T):
    N, M, A, B = map(int, input().split())
    a, m = solve(N, M, A, B)
    if not a:
        print('NO')
    else:
        print('YES')
        for row in m:
            print(''.join(map(str, row)))


