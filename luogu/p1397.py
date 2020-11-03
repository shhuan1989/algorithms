# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/16

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

import math

if __name__ == '__main__':
    # sys.setrecursionlimit(20000000)
    # sys.stdin = open('P1397_9.in', 'r')
    N, M, A, B, C, D = input().split()
    A, B, C, D = int(A), int(B), int(C), int(D)
    
    MOD = 10**9+7
    
    m = MOD-1 if A != 1 and C != 1 else MOD
    
    NN = 0
    for ch in N:
        NN = (NN*10 + int(ch)) % m
    
    MM = 0
    for ch in M:
        MM = (MM*10 + int(ch)) % m
    
    N, M = NN, MM
    

    # print(math.log(N), math.log(M))
    # if A != 1 and C != 1:
    #     N %= MOD-1
    #     M %= MOD-1
    # else:
    #     N %= MOD
    #     M %= MOD
    # print(math.log(N), math.log(M))
    
    def matmul(a, b):
        n, m, k = len(a), len(a[0]), len(b[0])
        ret = [[0 for _ in range(k)] for _ in range(n)]
        
        for r in range(n):
            for c in range(k):
                row = a[r]
                col = [b[x][c] for x in range(m)]
                ret[r][c] = sum([x*y for x, y in zip(row, col)]) % MOD
                
        return ret
    
    # def matmul(a, b):
    #     ret = [[0, 0], [0, 0]]
    #     ret[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
    #     ret[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
    #     ret[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
    #     ret[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
    #     
    #     return ret
    
    def mypowa(mat, p):
        if p == 1:
            return mat
    
        a = mypowa(mat, p // 2)
        b = matmul(a, a)
        if p % 2 == 1:
            b = matmul(b, mat)

        return b
        
    def mypow(mat, p):
        ret = [[1, 0], [0, 1]]
        
        while p > 0:
            if p & 1 > 0:
                ret = matmul(ret, mat)
            mat = matmul(mat, mat)
            p >>= 1
        
        return ret
        
    
    
    
    
    # mem = [[0 for _ in range(M+1)] for _ in range(N+1)]
    #
    # mem[1][1] = 1
    # for r in range(1, N+1):
    #     mem[r][1] = (C * mem[r-1][M] + D) if r > 1 else 1
    #     for c in range(2, M+1):
    #         mem[r][c] = A * mem[r][c-1] + B
    #
    #
    # for r in range(1, N+1):
    #     print(' '.join(map(str, mem[r][1:])))
        
    
    
    # f(1, 1) => f(1, n)
    # f(2, 1) = f(1, n) * []
    # f(2, 1) => f(2, n)
    # ...
    
    
    ma = [
            [A, 0],
            [B, 1]
        ]
    
    mb = mypow(ma, M-1)
    
    mc = [
        [C, 0],
        [D, 1],
    ]
    
    md = matmul(mc, mb)
    
    me = mypow(md, N-1)
    
    ret = matmul([[1, 1]], mb)
    # print('x', ret)
    # print('me', me)
    ret = matmul(ret, me)
    
    # print('x', ret)
    print(ret[0][0])
    
    
    # prev = 1
    # for i in range(1, N+1):
    #     start = (C * prev + D) if i > 1 else 1
    #
    #     mat = [
    #         [A, 0],
    #         [B, 1]
    #     ]
    #
    #     ret = [[start, 1]]
    #
    #     ret = matmul(ret, mypow(mat, M-1))
    #
    #     prev = ret[0][0]
    #
    # print(prev)
    #
    
