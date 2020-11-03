# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/21

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    MOD = 1000000007
    
    initstate = [False for _ in range(64)]
    transmat = [[0 for _ in range(64)] for _ in range(64)]
    bin = [0, 1]
    for i in range(2, 6):
        bin.append(bin[i-1] << 1)
    
    def inittrans(state, count):
        initstate[state] = True
        prestate = state >> 1
        transmat[prestate][state] = 1
        
        if count == K and (state & 1) == 0:
            return
        transmat[prestate + bin[M]][state] = 1
        
    def dfs(index, count, state):
        if index >= M+1:
            inittrans(state, count)
            return
        dfs(index+1, count, state)
        if count < K:
            dfs(index+1, count+1, state | bin[index])
    
    def matmul(a, b):
        c = [[0 for _ in range(64)] for _ in range(64)]
        lim = 1 << M
        for i in range(lim):
            for j in range(lim):
                for k in range(lim):
                    c[i][j] += a[i][k] * b[k][j]
                    c[i][j] %= MOD
                    
        return c
    
    def matpow():
        n = N
        bj = False
        ret = [[0 for _ in range(64)] for _ in range(64)]
        x = transmat
        while n > 0:
            if n & 1:
                if not bj:
                    ret = x
                    bj = True
                else:
                    ret = matmul(ret, x)
            x = matmul(x, x)
            n >>= 1
        
        return ret
                    
    
    
    dfs(1, 0, 0)
    ret = matpow()
    
    ans = 0
    
    for i in range(1 << M):
        if initstate[i]:
            ans += ret[i][i]
            ans %= MOD
    print(ans)