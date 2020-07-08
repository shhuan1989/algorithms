# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/1

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
e

def solve(N, M, A, B):
    K = N * M
    L = 1
    while 2 ** L < K:
        L += 1
        
    def toid(r, c):
        return r*M+c
    
    def torc(id):
        r, c = id // M, id % M
        return r, c
        
    endpoint = [[i for _ in range(2)] for i in range(K)]
    for i in range(K):
        r, c = torc(i)
        d = B[r][c]
        if d == 'U':
            endpoint[i][0] = toid(r-1, c)
        elif d == 'D':
            endpoint[i][0] = toid(r+1, c)
        elif d == 'L':
            endpoint[i][0] = toid(r, c-1)
        else:
            endpoint[i][0] = toid(r, c+1)
    
    for l in range(1, L+1):
        for i in range(K):
            endpoint[i][l % 2] = endpoint[endpoint[i][(l+1)%2]][(l+1)%2]
    
    start = collections.defaultdict(list)
    for i in range(K):
        start[endpoint[i][L%2]].append(i)
    
    a = len(start)
    b = 0
    for points in start.values():
        for i in points:
            r, c = torc(i)
            if A[r][c] == '0':
                b += 1
                break
                
    return a, b


if __name__ == '__main__':
    T = int(input())
    ans = []
    for ti in range(T):
        N, M = map(int, input().split())
        A = []
        for i in range(N):
            A.append(input())
        B = []
        for i in range(N):
            B.append(input())
        
        ans.append(solve(N, M, A, B))
    
    print('\n'.join(['{} {}'.format(a, b) for a, b in ans]))