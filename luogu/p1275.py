# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/21

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



def dfs(index, rest, swapped, ca):
    if index >= M:
        return True
    
    for c in rest:
        if ca[c] == CB[index]:
            if all([(A[r][c] if r not in swapped else A[r][c] ^ 1) == B[r][index] for r in range(N)]):
                rest.remove(c)
                if dfs(index + 1, rest, swapped, ca):
                    return True
                rest.add(c)
    
    return False


def solve(N, M, A):
    col0 = [B[r][0] for r in range(N)]
    s0 = sum(col0)
    for i in range(M):
        # match ith col to the first col
        col = [A[r][i] for r in range(N)]
        s = sum(col)
        if s != s0 and s != N-s0:
            continue
        
        swapped = set()
        for r in range(N):
            if col0[r] != col[r]:
                swapped.add(r)
        
        ca = []
        for c in range(M):
            v = sum([A[r][c] ^ 1 if r in swapped else A[r][c] for r in range(N)])
            ca.append(v)
        
        if dfs(1, [c for c in range(M) if c != i], swapped, ca):
            return True
        
    return False


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        A = []
        for _ in range(N):
            row = [int(x) for x in input().split()]
            A.append(row)
        B = []
        for _ in range(N):
            row = [int(x) for x in input().split()]
            B.append(row)
        CB = []
        for c in range(M):
            CB.append(sum([B[r][c] for r in range(N)]))
        
        print('YES' if solve(N, M, A) else 'NO')