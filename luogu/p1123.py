# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/17

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def desc(state, N, M):
    
    a = [[0 for _ in range(M)] for _ in range(2)]
    
    for r in range(2):
        for c in range(M):
            a[r][c] = 1 if state & (1 << (r * M +c)) > 0 else 0
    
    for row in a:
        print(' '.join(map(str, row)))
    
    return a


# row2 + row1
def getrow2(state, M):
    return state >> M

def getrow1(state, M):
    return state & ((1 << M) - 1)

def fillrow2(state, M, i):
    return state | (1 << (M+i))

def issetrow2(state, M, i):
    return state & (1 << (M+i)) > 0

def issetrow1(state, M, i):
    return state & (1 << i) > 0

def solve(N, M, A):
    MAXS = 2 ** (2 * M)
    dp = [[[0 for _ in range(MAXS)] for _ in range(M)] for _ in range(N)]
    
    dp[0][0][fillrow2(0, M, 0)] = A[0][0]
    
    for r in range(N):
        for c in range(M):
            if r > 0 and c == 0:
                for s in range(MAXS):
                    if any([issetrow2(s, M, i) for i in range(1, M)]):
                        continue
                    for ps in range(MAXS):
                        if getrow1(s, M) == getrow2(ps, M):
                            if issetrow2(s, M, 0):
                                if issetrow2(ps, M, 0) or issetrow2(ps, M, 1):
                                    pass
                                else:
                                    for pc in range(M):
                                        dp[r][c][s] = max(dp[r][c][s], dp[r - 1][pc][ps] + A[r][0])
                            else:
                                for pc in range(M):
                                    dp[r][c][s] = max(dp[r][c][s], dp[r - 1][pc][ps])
                            
                continue
                
            if c > 0:
                for s in range(MAXS):
                    dp[r][c][s] = dp[r][c-1][s]
            for s in range(MAXS):
                if c > 0:
                    if issetrow1(s, M, c-1) or issetrow2(s, M, c-1):
                        continue
                if issetrow1(s, M, c) or issetrow2(s, M, c):
                    continue
                if c+1 < M:
                    if issetrow1(s, M, c+1) or issetrow2(s, M, c+1):
                        continue
                
                if any([issetrow2(s, M, i) for i in range(c, M)]):
                    continue
                    
                ns = fillrow2(s, M, c)
                dp[r][c][ns] = max(dp[r][c][ns], (dp[r][c-1][s] if c-1 >= 0 else 0) + A[r][c])
                
    return max(dp[N-1][M-1])


VIS = [False for _ in range(50)]

def getvindex(M, r, c):
    return r*M+c

ANS = [0]

def dfs(N, M, A, r, c, pre, rest):
    if r >= N:
        ANS[0] = max(ANS[0], pre)
        return pre
    
    if pre + rest < ANS[0]:
        return pre
    
    valid = True
    vi = getvindex(M, r, c)
    for x, y in [(r-1, c-1), (r, c-1), (r-1, c), (r-1, c+1)]:
        if 0 <= x < N and 0 <= y < M and (x, y) and VIS[getvindex(M, x, y)]:
            valid = False
            break
    ans = 0
    nr, nc = (r, c + 1) if c + 1 < M else (r+1, 0)
    if valid:
        VIS[vi] = True
        ans = max(ans, dfs(N, M, A, nr, nc, pre + A[r][c], rest-A[r][c]))
        VIS[vi] = False
        
    ans = max(ans, dfs(N, M, A, nr, nc, pre, rest-A[r][c]))
    
    return ans


def solve2(N, M, A):
    ANS[0] = 0
    sa = sum([sum(row) for row in A])
    return dfs(N, M, A, 0, 0, 0, sa)


if __name__ == '__main__':
    T = int(input())
    for ti in range(T):
        N, M = map(int, input().strip().split())
        A = []
        for i in range(N):
            row = [int(x) for x in input().strip().split()]
            A.append(row)
        
        print(solve2(N, M, A))